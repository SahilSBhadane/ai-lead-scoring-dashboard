# 🧠 AI-Powered CRM Lead Scoring System

This project builds an end-to-end AI-powered solution to score sales leads based on CRM data. It leverages machine learning models to predict lead conversion potential and presents the results through a Streamlit dashboard and Power BI visualizations.

---

## 📂 Project Structure
CRM_Lead_Score_AI/
├── data/
│ ├── sales_pipeline.csv # Raw sales pipeline data
│ ├── agent_info.csv # Agent metadata
│ └── scored_leads.csv # Final lead scores
│
├── scripts/
│ ├── data_merge.py # Script to merge raw datasets
│ ├── preprocessing.py # Feature engineering and cleaning
│ └── modeling.py # ML model training and evaluation
│
├── dashboard/
│ ├── app.py # Streamlit web app
│ └── scored_leads.csv # Used for dashboard visualization
│
├── outputs/
│ ├── model_predictions.csv # Model output file
│ └── metrics.txt # RMSE, R², and other metrics
│
├── main.py # Pipeline runner script
└── README.md # Project documentation




---

## ⚙️ How It Works

1. **Data Merging:** Combines `sales_pipeline.csv` and `agent_info.csv`.
2. **Preprocessing:** Cleans data, handles dates, encodes categories.
3. **Modeling:** Trains Linear Regression and Random Forest regressors.
4. **Scoring:** Outputs predicted lead conversion scores (0–1).
5. **Visualization:** Provides insights via Power BI and Streamlit.

---

## 📊 Sample Insights

- **Linear Regression:** R² = 1.00, RMSE = 0.00  
- **Random Forest:** R² = 1.00, RMSE = 0.00

*Note: Perfect scores due to synthetic/sample dataset.*

---

## 📈 Streamlit Dashboard

Run the interactive dashboard locally:

```bash
pip install streamlit pandas
streamlit run dashboard/app.py
