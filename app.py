# app.py
import streamlit as st
import pandas as pd
from fetch_data import fetch_agri_data, list_supported_states, get_rainfall_timeseries, compare_states_rainfall, get_rainfall_latest
from chat_agent_groq import ask_groq_with_context
from qa_engine import generate_data_insight
import plotly.express as px

st.set_page_config(page_title="AgriInsight", layout="wide", page_icon="🌾")
st.title("AgriInsight — Groq + Data.gov + Live Climate")

# Sidebar: choose section
section = st.sidebar.radio("Select", ["Chatbot", "Data Explorer", "Rainfall & Climate"])

# ----------------- Chatbot -----------------
if section == "Chatbot":
    st.header("🤖 Groq Chatbot (uses gov context)")
    q = st.text_area("Ask anything (agriculture, climate):", height=120)
    if st.button("Ask Groq"):
        if not q.strip():
            st.warning("Type a question first.")
        else:
            with st.spinner("Thinking with Groq..."):
                ans = ask_groq_with_context(q)
                st.markdown("**Answer:**")
                st.write(ans)

# ----------------- Data Explorer -----------------
elif section == "Data Explorer":
    st.header("📊 Data Explorer — Data.gov crop dataset")
    with st.spinner("Loading Data.gov crop dataset..."):
        df = fetch_agri_data(limit=500)

    if df is None or df.empty:
        st.error("No data loaded. Try later or provide DATA_GOV_API_KEY in .env for full access.")
    else:
        st.success(f"Loaded {len(df)} records.")
        st.dataframe(df.head(200))

        cols = list(df.columns)
        st.markdown("**Filters**")
        if "state" in df.columns:
            sel_states = st.multiselect("State", sorted(df["state"].dropna().unique()))
        else:
            sel_states = []
        if "commodity" in df.columns:
            sel_crops = st.multiselect("Crop", sorted(df["commodity"].dropna().unique()))
        else:
            sel_crops = []

        filtered = df.copy()
        if sel_states:
            filtered = filtered[filtered["state"].isin(sel_states)]
        if sel_crops:
            filtered = filtered[filtered["commodity"].isin(sel_crops)]

        st.write(f"Showing {len(filtered)} records")
        st.dataframe(filtered.head(500))

        st.markdown("---")
        st.subheader("Ask data-specific questions (deterministic)")
        data_q = st.text_input("E.g., Which state has highest production?")
        if st.button("Analyze data"):
            if not data_q.strip():
                st.warning("Enter a question.")
            else:
                with st.spinner("Analyzing..."):
                    insight = generate_data_insight(data_q, filtered)
                    st.success(insight)

# ----------------- Rainfall & Climate -----------------
else:
    st.header("🌦 Rainfall & Climate")
    states = list_supported_states()
    s1 = st.selectbox("State A", states, index=0)
    s2 = st.selectbox("State B", states, index=1 if len(states) > 1 else 0)
    days = st.slider("Days of history", min_value=30, max_value=365, value=90, step=30)
    if st.button("Compare rainfall"):
        with st.spinner("Fetching rainfall timeseries..."):
            df1, err1 = get_rainfall_timeseries(s1, days=days)
            df2, err2 = get_rainfall_timeseries(s2, days=days)
            if err1 or err2 or df1 is None or df2 is None:
                st.error(f"Error fetching rainfall: {err1 or err2}")
            else:
                df1["state"] = s1
                df2["state"] = s2
                merged = pd.concat([df1, df2], ignore_index=True)
                fig = px.line(merged, x="date", y="precip_mm", color="state",
                              title=f"Daily rainfall last {days} days")
                st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.subheader("Latest rainfall (sample states)")
    try:
        r1, e1 = get_rainfall_latest(s1)
        r2, e2 = get_rainfall_latest(s2)
        col1, col2 = st.columns(2)
        with col1:
            if r1:
                st.metric(f"{r1['state']} latest rainfall (mm)", f"{r1['latest_rainfall_mm']}")
            else:
                st.write("No data.")
        with col2:
            if r2:
                st.metric(f"{r2['state']} latest rainfall (mm)", f"{r2['latest_rainfall_mm']}")
            else:
                st.write("No data.")
    except Exception as ex:
        st.error(str(ex))

    st.markdown("---")
    st.subheader("Compare average rainfall across multiple states (last 30 days)")
    selected = st.multiselect("Choose states to compare", states, default=states[:3])
    if st.button("Compare averages"):
        with st.spinner("Computing averages..."):
            comp = compare_states_rainfall(selected, days=30)
            st.dataframe(comp)
            fig2 = px.bar(comp, x="state", y="avg_rain_mm", title="Avg rainfall (last 30 days)")
            st.plotly_chart(fig2, use_container_width=True)
