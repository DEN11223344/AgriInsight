# fetch_data.py
import os
import requests
import pandas as pd
from datetime import date, timedelta
from dotenv import load_dotenv

load_dotenv()

# Optional Data.gov API key
DATA_GOV_API_KEY = os.getenv("DATA_GOV_API_KEY")

# Mapping of state -> representative lat/lon
STATE_COORDS = {
    "Maharashtra": (19.7515, 75.7139),
    "Karnataka": (15.3173, 75.7139),
    "Kerala": (10.8505, 76.2711),
    "Gujarat": (22.2587, 71.1924),
    "Tamil Nadu": (11.1271, 78.6569),
    "Punjab": (31.1471, 75.3412),
    "Pune": (18.5204, 73.8567)  # city example
}

# -----------------------------
# Data.gov: crop / production dataset
# -----------------------------
def fetch_agri_data(limit=500):
    """
    Returns a pandas DataFrame with records (state, district, commodity, production, year, etc.)
    Falls back to empty DataFrame on failure.
    """
    try:
        base = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"
        params = {"format": "json", "limit": limit}
        if DATA_GOV_API_KEY:
            params["api-key"] = DATA_GOV_API_KEY

        r = requests.get(base, params=params, timeout=12)
        r.raise_for_status()

        data = r.json()
        records = data.get("records", [])
        if not records:
            return pd.DataFrame()

        df = pd.DataFrame(records)
        df.columns = [c.lower() for c in df.columns]

        keep = [c for c in ["state", "district", "commodity", "crop", "production", "year", "variety"] if c in df.columns]
        if not keep:
            return df
        return df[keep].copy()

    except Exception as e:
        print("⚠️ Error fetching Data.gov:", e)
        return pd.DataFrame()

# -----------------------------
# Open-Meteo: rainfall/time-series helpers (FIXED)
# -----------------------------
def get_rainfall_timeseries(state_or_coord, days=365):
    """
    Return a DataFrame with daily precipitation_sum for the last `days`.
    Uses the /v1/forecast endpoint (since /v1/era5 is deprecated).
    """
    try:
        if isinstance(state_or_coord, str):
            if state_or_coord not in STATE_COORDS:
                return None, f"Unsupported state: {state_or_coord}"
            lat, lon = STATE_COORDS[state_or_coord]
        else:
            lat, lon = state_or_coord

        end = date.today()
        start = end - timedelta(days=days)

        url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}"
            f"&start_date={start.isoformat()}&end_date={end.isoformat()}"
            f"&daily=precipitation_sum&timezone=auto"
        )

        r = requests.get(url, timeout=12)
        r.raise_for_status()
        j = r.json()

        daily = j.get("daily", {})
        dates = daily.get("time", [])
        precip = daily.get("precipitation_sum", [])

        if not dates or not precip:
            return None, "No rainfall timeseries returned."

        df = pd.DataFrame({
            "date": pd.to_datetime(dates),
            "precip_mm": precip
        })
        return df, None

    except Exception as e:
        return None, str(e)

def get_rainfall_latest(state):
    """Return the latest daily rainfall value (mm) for a state"""
    df, err = get_rainfall_timeseries(state, days=7)
    if err or df is None or df.empty:
        return None, err
    latest = df.iloc[-1]
    return {"state": state, "latest_rainfall_mm": float(latest["precip_mm"])}, None

def compare_states_rainfall(states, days=30):
    """Return a DataFrame comparing avg rainfall over last `days` for each state."""
    rows = []
    for s in states:
        ts, err = get_rainfall_timeseries(s, days=days)
        if ts is None or ts.empty:
            rows.append({"state": s, "avg_rain_mm": None, "error": err})
            continue
        rows.append({
            "state": s,
            "avg_rain_mm": round(float(ts["precip_mm"].mean()), 2),
            "error": None
        })
    return pd.DataFrame(rows)

# -----------------------------
# Convenience
# -----------------------------
def list_supported_states():
    """List all available states / cities for rainfall data"""
    return list(STATE_COORDS.keys())
