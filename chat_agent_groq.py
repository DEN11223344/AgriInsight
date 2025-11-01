# chat_agent_groq.py
import os
import pandas as pd
import requests
from groq import Groq
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
from fetch_data import fetch_agri_data  # use the fetch_data above

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("Missing GROQ_API_KEY in .env")

client = Groq(api_key=GROQ_API_KEY)

# Build doc store from gov dataset (with fallback)
DOCS = []
try:
    df_gov = fetch_agri_data(limit=500)
    if not df_gov.empty:
        # build compact text per row
        def row_text(r):
            s = r.get("state", "") or r.get("state")
            d = r.get("district", "") or r.get("district")
            crop = r.get("commodity", r.get("crop", ""))
            prod = r.get("production", "")
            return f"{s} | {d} | Crop: {crop} | Production: {prod}"
        DOCS = df_gov.apply(row_text, axis=1).tolist()
except Exception:
    DOCS = []

if not DOCS:
    DOCS = [
        "Maharashtra | Pune | Crop: Sugarcane | Production: High",
        "Karnataka | Belgaum | Crop: Rice | Production: Medium",
        "Kerala | Thrissur | Crop: Coconut | Production: High",
    ]

VEC = TfidfVectorizer(stop_words="english").fit(DOCS)
DOC_VECTORS = VEC.transform(DOCS)


def retrieve(query, k=3):
    qv = VEC.transform([query])
    sims = cosine_similarity(qv, DOC_VECTORS).flatten()
    top_idxs = sims.argsort()[-k:][::-1]
    return [DOCS[i] for i in top_idxs]


def ask_groq_with_context(query):
    """
    Uses Groq LLM with TF-IDF retrieved context from data.gov.
    Returns text answer (string).
    """
    contexts = retrieve(query, k=4)
    prompt = "Context:\n" + "\n".join(contexts) + f"\n\nQuestion: {query}\nAnswer concisely and cite context rows when relevant."
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # recommended stable model
            messages=[
                {"role": "system", "content": "You are AgriInsight — an expert assistant for Indian agriculture."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ Groq API Error: {e}"
