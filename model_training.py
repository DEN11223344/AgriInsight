import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import joblib
from fetch_data import fetch_data

df = fetch_data()

df = df[['state', 'district', 'market', 'commodity', 'variety', 'min_price', 'max_price', 'modal_price']]
df = df.dropna()

# Convert prices to numeric
for col in ['min_price', 'max_price', 'modal_price']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df = df.dropna()

# Encode categorical columns
le = LabelEncoder()
for col in ['state', 'district', 'market', 'commodity', 'variety']:
    df[col] = le.fit_transform(df[col])

X = df[['state', 'district', 'market', 'commodity', 'variety', 'min_price', 'max_price']]
y = df['modal_price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, "model.pkl")
print("✅ Model trained and saved as model.pkl")
