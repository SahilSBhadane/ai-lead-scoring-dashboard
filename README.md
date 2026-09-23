# CRM Lead Scoring

Predicts the **win probability of open sales deals** from CRM pipeline data and ranks them in a Streamlit dashboard, so a sales team knows which deals to work first.

**Stack:** Python · pandas · scikit-learn · XGBoost · Streamlit

## How it works

```
sales_pipeline + accounts + products + sales_teams
        │  join (scripts/data_merge.py)
        ▼
closed deals (Won / Lost) ──► train + evaluate ──► best model by CV ROC-AUC
open deals (Engaging / Prospecting) ─────────────► score ──► outputs/scored_leads.csv ──► dashboard
```

1. **Join** the four CRM tables onto the sales pipeline (and fix the typos / product-name mismatches in the raw files).
2. **Label** only closed deals: `won = 1` if Won, `0` if Lost. Open deals have no outcome yet, so they are what gets scored.
3. **Features** are limited to what's known *before* a deal closes: agent, manager, region, product, series, price, account sector / size / age, engage month and weekday.
4. **Models:** majority-class baseline vs Logistic Regression vs XGBoost, in scikit-learn pipelines (one-hot encoding + imputation), 5-fold stratified CV on ROC-AUC, plus a held-out test set.
5. The best model is refit on all closed deals and used to score the open pipeline into High / Medium / Low priority.

## Avoiding target leakage

An earlier version of this project reported R² = 1.00. That score was a bug: `close_value` (used to build the label) and `deal_stage` (which *is* the label) were still in the features, so the model was handed the answer. This version:

- drops `deal_stage`, `close_date` and `close_value` from the features
- treats it as **classification** (win / lose), not regression
- evaluates with ROC-AUC and PR-AUC against a baseline instead of R²

## Results

Run `python main.py`. Metrics are written to `outputs/metrics_report.txt`.

<!-- Paste the metrics table from outputs/metrics_report.txt here after running -->

Honest note: pre-close CRM fields carry limited signal about whether a deal is won, so expect a modest ROC-AUC. The point of this project is a correct, leak-free pipeline, not a headline number.

## Run it

Dataset: Maven Analytics **CRM + Sales + Opportunities** (free). Put `sales_pipeline.csv`, `accounts.csv`, `products.csv` and `sales_teams.csv` in `data/`.

```bash
pip install -r requirements.txt
python main.py                      # train, evaluate, score open deals
streamlit run dashboard/app.py      # dashboard
```

## Structure

```
main.py                 # end-to-end run
scripts/data_merge.py   # load + join tables
scripts/preprocessing.py# labels, features, leak-prone columns
scripts/modeling.py     # baseline / Logistic Regression / XGBoost + evaluation
dashboard/app.py        # Streamlit dashboard
```
