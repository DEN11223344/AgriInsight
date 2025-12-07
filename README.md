🌾 AgriInsight AI — Smart Agriculture Decision Support System

AgriInsight AI is an interactive machine learning–powered decision support system designed to help farmers, researchers, and agricultural planners make data-driven crop decisions.
The system analyzes climate patterns, soil characteristics, and environmental conditions to recommend the most suitable crops, predict yield potential, and assist in improving sustainable farming outcomes.

🚀 Features

🌱 Crop Recommendation Engine based on soil nutrients, rainfall, temperature, pH, humidity, and climatic zone

📈 Yield Prediction Model using machine learning (Random Forest / XGBoost)

🛰 Live Weather & Climate Integration using external API

🚦 Soil Health Scoring (NPK balance, pH fitness, moisture fitness)

🧠 Explainable AI (XAI) Insights showing feature importance behind predictions

📊 Interactive Visual Dashboard to analyze patterns, compare crops, and visualize trends

🏭 Sustainability-focused insights including irrigation needs, fertilizer suggestions, and environmental impact indicators

📄 Downloadable PDF Advisory Report for field use

⚡ Fully deployed as a Streamlit Web App

🧠 Machine Learning Models Used
Task	Model Used	Why
Crop Recommendation	Random Forest / SVM	Handles non-linear relationships & categorical features
Yield Prediction	XGBoost Regression	Robust, high accuracy and handles environmental variability
Soil Suitability Scoring	Rule-based + ML hybrid	Balances scientific thresholds with learning patterns
📂 Dataset Sources

Indian State Agriculture Databank (Soil + Crop Suitability)

FAO Climate Crop Suitability Records

Kaggle Open Agricultural Datasets

Local weather history from OpenWeather API / rainfall records

(Used for training, evaluation and benchmarking.)

🛠 Tech Stack
Component	Technology
Frontend	Streamlit
Backend	Python
ML & Analytics	Pandas, NumPy, Scikit-Learn, XGBoost
Visualization	Plotly, Matplotlib, Seaborn
Optional Live Data	OpenWeather API / AgroAPI
Model Deployment	Pickle (.pkl model)
📦 Installation
git clone https://github.com/YOUR-USERNAME/AgriInsight-AI.git
cd AgriInsight-AI
pip install -r requirements.txt

▶️ Run the App
streamlit run app.py


App will launch in your browser automatically.

📊 UI Preview

(Add later if you upload screenshot)

📈 Model Evaluation

Accuracy: ~92–96% (Crop Recommendation)

R² Score: ~0.80–0.90+ (Yield Model)

Cross-validation used for robustness

Feature importance & SHAP values included for transparency

🧪 Example Use Cases

Farmers deciding which crop to grow based on soil test reports

Agri officers evaluating crop planning region-wise

Students and researchers exploring environmental impact on agriculture

NGOs promoting sustainable agriculture and resource planning

Smart farming and precision agriculture systems

📄 Outputs Provided

Best crop recommendations for input conditions

Expected yield and confidence range

Fertilizer recommendation and soil improvement suggestions

Weather-dependent advisories (rainfall, irrigation, sowing time)

PDF advisory report for offline usage

🤝 Contributing

Pull requests and dataset improvements are welcome — especially region-specific crop datasets.

📜 License

This project is licensed under the MIT License.

👤 Author

Piyush Balode
Machine Learning & Applied AI

⭐ If you find this helpful, please give the repository a star — it supports open agricultural innovation 🌍
