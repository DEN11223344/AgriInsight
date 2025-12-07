🌾 AgriInsight AI

🎯 AI-Powered Smart Agriculture Decision Support System

AgriInsight AI is an intelligent, machine-learning–based platform designed to help farmers, agricultural officers, and researchers make data-driven crop and farming decisions.
The system analyzes environmental factors like soil nutrients, rainfall, temperature, humidity, and weather conditions to generate:

🌱 Best crop recommendations

📈 Yield predictions

💧 Irrigation and soil improvement suggestions

🧪 Fertilizer guidance and sustainability insights

📌 This version focuses on crop recommendation and yield prediction using live data and ML models.
🚜 Future version will include pest prediction, disease detection, and region-wise forecasting.

🚀 Features
Feature	Description
✔️ Crop Recommendation System	Suggests suitable crops based on environmental + soil profiles
📈 Yield Prediction	Uses ML regression models to estimate expected yield
🌍 Live Weather Integration	Fetches real-time weather (temperature, humidity, rainfall)
🧪 Soil Suitability Score	Evaluates NPK levels, pH, moisture, carbon balance
💧 Resource Advisory	Suggests irrigation level, fertilizer composition & sowing window
📊 Visual Analytics Dashboard	Interactive charts for climate trends and soil comparison
📄 Downloadable PDF Report	Generates a field-ready advisory sheet
🧩 Tech Stack
🔹 Backend + AI Models

Python

Scikit-Learn

XGBoost

Pandas, NumPy

Pickle model deployment

🔹 Frontend / Deployment

Streamlit

Plotly (interactive visualizations)

🔹 Optional Integrations

Weather API (OpenWeather API)

AQI layer (if available)

🔬 Machine Learning Models Used
Task	Model	Purpose
Crop Recommendation	Random Forest / SVM	Handles feature interactions and categorical environmental variables
Yield Prediction	XGBoost Regression	High accuracy and robust to non-linear agriculture data
Soil Fitness Scoring	Hybrid ML + Rule-based	Balances AI insights with agronomic science
⚙️ Installation & Setup
🔧 Clone the Repository
git clone https://github.com/YOUR-USERNAME/AgriInsight-AI.git
cd AgriInsight-AI

🛠 Install Dependencies
pip install -r requirements.txt

▶️ Run the Application
streamlit run app.py


🌍 App will start at:

http://localhost:8501

📂 Folder Structure
AgriInsight-AI/
│
├── app.py                      # Main Streamlit app
├── models/
│   ├── crop_recommendation.pkl
│   └── yield_prediction.pkl
│
├── data/
│   └── sample_dataset.csv
│
├── requirements.txt
└── README.md

📚 Dataset Used

The dataset was built using:

Indian agricultural soil and crop mapping sources

Open-source crop suitability datasets

Climate records (temperature, rainfall, humidity trends)

Local soil test values (NPK, pH, organic carbon)

📊 Evaluation Results
Model	Metric	Performance
Random Forest (Crop Recommendation)	Accuracy	⭐ 93–96%
XGBoost Regression (Yield Prediction)	R² Score	⭐ 0.82–0.90+
Soil Fitness System	Evaluation	Supports agronomic threshold validation
🧑‍🌾 Use Cases

Farmer advisory dashboards

Smart agriculture & IoT automation

Region-wise farming policy insights

Agriculture education and research

Precision farming systems

📄 Outputs Generated

Best crop options ranked by suitability

Expected yield estimation with confidence

Fertilizer + irrigation recommendation

Weather-aware sowing schedule

Downloadable advisory report

👨‍💻 Contributor
Name	Role
Piyush Balode	Research, Model Development, System Design, Deployment
🧾 License

This project is intended for educational and research use only.
Not recommended as a standalone commercial agricultural advisory system.

🌟 Final Note

AgriInsight AI aims to bridge the gap between technology and farming, helping improve productivity, crop selection, and environmental sustainability through accessible AI-driven guidance.

⭐ If you find this project helpful, please give it a star!
