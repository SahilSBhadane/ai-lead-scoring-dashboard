# 🧠 AI-Powered CRM Lead Scoring System

This project builds an end-to-end AI-powered solution to score sales leads based on CRM data. It leverages machine learning models to predict lead conversion potential and presents the results through a Streamlit dashboard and Power BI visualizations.

---

## 📁 Project Structure

CRM_Leading_Score/
│
├── data/
│ ├── sales_pipeline.csv
│ ├── agent_info.csv
│ └── scored_leads.csv # Final predictions
│
├── scripts/
│ ├── data_merge.py # Merges raw datasets
│ ├── preprocessing.py # Feature engineering
│ └── modeling.py # ML training & evaluation
│
├── dashboard/
│ ├── app.py # Streamlit app
│ └── scored_leads.csv # Used in dashboard
│
├── outputs/
│ ├── metrics.txt # RMSE & R² results
│ └── model_predictions.csv
│
├── main.py # Pipeline runner script
└── README.md # You're reading it!



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
