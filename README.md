# 🧠 AI-Powered CRM Lead Scoring System

This project builds an end-to-end AI-powered solution to score sales leads based on CRM data. It leverages machine learning models to predict lead conversion potential and presents the results through a Streamlit dashboard and Power BI visualizations.

---

## 📁 Project Structure

CRM_Leading_Score/
├── data/
│   ├── sales_pipeline.csv         # Raw opportunity data
│   ├── agent_info.csv             # Sales agent metadata
│   └── scored_leads.csv           # Final scored leads
│
├── scripts/
│   ├── data_merge.py              # Merges and aligns raw datasets
│   ├── preprocessing.py           # Feature engineering and encoding
│   └── modeling.py                # ML model training & evaluation
│
├── dashboard/
│   ├── app.py                     # Streamlit dashboard code
│   └── scored_leads.csv           # Input for dashboard (can be symlinked)
│
├── outputs/
│   ├── metrics.txt                # RMSE and R² scores
│   └── model_predictions.csv      # Model output scores
│
├── main.py                        # Pipeline runner script
└── README.md                      # Project documentation (this file)





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
