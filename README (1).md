# 🌾 AgriInsight AI

A professional, AI-driven decision support system for precision agriculture. AgriInsight AI combines environmental, soil, and weather data with machine learning to provide crop recommendations, yield predictions, and actionable agronomic guidance.

---

## ✨ Project Summary

AgriInsight AI helps farmers, extension officers, and researchers make data-driven decisions by analyzing soil nutrients (NPK, pH, organic carbon), local climate (temperature, humidity, rainfall), and other environmental variables. The current release focuses on crop recommendation and yield prediction; future releases plan to add pest and disease prediction, and region-wise forecasting.

---

## 🚀 Key Features

| Emoji | Feature | Description |
|---:|---|---|
| ✔️ | Crop Recommendation | Suggests optimal crops based on soil and environmental profiles. |
| 📈 | Yield Prediction | Uses advanced regression models to estimate expected yields with confidence intervals. |
| 🌦️ | Live Weather Integration | Fetches real-time weather (temperature, humidity, rainfall) for improved recommendations. |
| 🧪 | Soil Fitness Scoring | Evaluates NPK, pH, moisture, and organic carbon using a hybrid ML + rule-based approach. |
| 💧 | Resource Advisory | Recommends irrigation levels, fertilizer composition, and sowing windows. |
| 📊 | Visual Analytics | Interactive charts and dashboards for trend analysis and comparisons. |
| 📄 | PDF Reports | Generates downloadable advisory reports for field use. |

---

## 🧩 Technology Stack

| Layer | Tools / Libraries |
|---|---|
| Backend & ML | Python, scikit-learn, XGBoost, pandas, NumPy |
| Model Serialization | Pickle |
| Frontend & Visualization | Streamlit, Plotly |
| Integrations | OpenWeather (weather API), optional AQI layer |
| Dev / Environment | requirements.txt for dependency management |

---

## 🧪 Machine Learning Models

| Task | Model(s) | Purpose |
|---|---|---|
| Crop Recommendation | Random Forest, SVM | Classify and rank crop suitability across environmental and soil features. |
| Yield Prediction | XGBoost Regression | Robust regression for non-linear relationships in agricultural data. |
| Soil Fitness | Hybrid ML + Rule-based | Combine model predictions with agronomic thresholds for actionable scoring. |

---

## ⚙️ Installation & Quick Start

1. Clone the repository
```bash
git clone https://github.com/DEN11223344/AgriInsight.git
cd AgriInsight
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the Streamlit application
```bash
streamlit run app.py
```

Access the app at: http://localhost:8501

---

## 📂 Repository Structure

```
AgriInsight/
├── app.py                      # Main Streamlit application
├── models/
│   ├── crop_recommendation.pkl
│   └── yield_prediction.pkl
├── data/
│   └── sample_dataset.csv
├── requirements.txt
└── README.md
```

---

## 📚 Data Sources

The dataset is compiled from a combination of:
- Indian agricultural soil and crop mapping sources
- Open-source crop suitability datasets
- Historical climate records (temperature, rainfall, humidity)
- Local soil test values (NPK, pH, organic carbon)

---

## 📈 Evaluation (Representative Results)

| Model | Metric | Typical Performance |
|---|---:|---|
| Random Forest (Crop Recommendation) | Accuracy | 93% – 96% |
| XGBoost (Yield Prediction) | R² Score | 0.82 – 0.90+ |
| Soil Fitness System | Agronomic validation | Aligns with established agronomic thresholds |

Note: Reported metrics are representative and depend on dataset quality and preprocessing.

---

## 🧑‍🌾 Use Cases

- Farmer advisory dashboards and farm management
- Precision irrigation and fertilizer scheduling (IoT integrations)
- Regional agricultural policy analysis and planning
- Research and education in agronomy and ML for agriculture

---

## 📄 Outputs

- Ranked list of best-fitting crops by suitability score
- Expected yield estimates with confidence
- Fertilizer and irrigation recommendations
- Weather-aware sowing schedule
- Downloadable advisory PDF for field use

---

## 👨‍💻 Contributor

| Name | Role |
|---|---|
| Piyush Balode | Research, model development, system design, deployment |

---

## 🧾 License & Disclaimer

This project is provided for educational and research purposes only. It is not intended to replace professional agronomic advice or be used as a sole source for commercial agricultural decisions. Users should validate recommendations with local agronomy experts.

---

## 🔭 Roadmap

- Add pest and disease prediction modules
- Region-wise forecasting and seasonal planning
- Enhanced model explainability and uncertainty quantification
- Mobile-friendly UI and IoT integrations

---

## 🤝 Contributing

Contributions, bug reports, and feature requests are welcome. Please open an issue or submit a pull request with a clear description and tests where applicable.

---

## ✉️ Contact

For questions or collaboration inquiries, open an issue or reach out to the maintainer via the repository.

Thank you for using AgriInsight AI — helping build sustainable and data-driven agriculture. 🌱