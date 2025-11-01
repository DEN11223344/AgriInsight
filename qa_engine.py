# qa.py
import pandas as pd

def generate_data_insight(query: str, df: pd.DataFrame):
    q = (query or "").lower()
    if df is None or df.empty:
        return "No data available to analyze."

    # ensure numeric production
    if "production" in df.columns:
        df2 = df.copy()
        df2["production"] = pd.to_numeric(df2["production"], errors="coerce")
    else:
        return "Dataset doesn't have a 'production' column to analyze."

    if "highest" in q or ("top" in q and "production" in q):
        grouped = df2.groupby("state")["production"].sum().sort_values(ascending=False)
        if grouped.empty:
            return "No production numbers to compare."
        state = grouped.index[0]
        val = grouped.iloc[0]
        return f"{state} has the highest total production: {val} (sum over available records)."

    if "lowest" in q:
        grouped = df2.groupby("state")["production"].sum().sort_values()
        if grouped.empty:
            return "No production numbers to compare."
        state = grouped.index[0]
        val = grouped.iloc[0]
        return f"{state} has the lowest total production: {val}."

    # basic crop top-M in a state
    if "top producers" in q or ("top producers" in q) or ("top" in q and "producers" in q):
        # try to extract crop and state keywords (very simple heuristic)
        tokens = q.split()
        # naive: look for 'in <state>'
        import re
        m = re.search(r"in ([a-zA-Z\s]+)$", q)
        state = m.group(1).strip().title() if m else None
        if state and "commodity" in df2.columns:
            sub = df2[df2["state"].str.lower() == state.lower()]
            if sub.empty:
                return f"No data for {state}."
            top = sub.groupby("commodity")["production"].sum().sort_values(ascending=False).head(5)
            return f"Top crops in {state} by production:\n" + ", ".join([f"{c} ({v})" for c, v in top.items()])
        else:
            return "Please ask like: 'Top producers of rice in Maharashtra'"

    return "Try asking about 'highest production', 'lowest production', or 'top producers of <crop> in <state>'."
