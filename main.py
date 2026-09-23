import os

import pandas as pd
from sklearn.model_selection import train_test_split

from scripts.data_merge import load_and_merge_data
from scripts.modeling import train_and_evaluate
from scripts.preprocessing import FEATURES, TARGET, split_closed_and_open


def tier(p):
    return "High" if p >= 0.7 else "Medium" if p >= 0.4 else "Low"


def main():
    os.makedirs("outputs", exist_ok=True)
    df = load_and_merge_data()
    closed, open_deals = split_closed_and_open(df)
    print(f"Closed deals: {len(closed)} (win rate {closed[TARGET].mean():.1%}) | "
          f"open deals to score: {len(open_deals)}")

    X_train, X_test, y_train, y_test = train_test_split(
        closed[FEATURES], closed[TARGET], test_size=0.2,
        stratify=closed[TARGET], random_state=42,
    )
    best_name, results = train_and_evaluate(X_train, X_test, y_train, y_test)

    # Metrics report
    rows = [{"model": n, **{k: round(v, 4) for k, v in r.items() if k != "model"}}
            for n, r in results.items()]
    report = pd.DataFrame(rows)
    report.to_csv("outputs/metrics_report.csv", index=False)
    with open("outputs/metrics_report.txt", "w") as f:
        f.write(f"Closed deals: {len(closed)} | win rate: {closed[TARGET].mean():.3f}\n")
        f.write(f"Selected model (best CV ROC-AUC): {best_name}\n\n")
        f.write(report.to_string(index=False))

    # Refit the chosen model on all closed deals, then score the OPEN pipeline
    model = results[best_name]["model"]
    model.fit(closed[FEATURES], closed[TARGET])
    open_deals["conversion_probability"] = model.predict_proba(open_deals[FEATURES])[:, 1].round(4)
    open_deals["priority"] = open_deals["conversion_probability"].apply(tier)
    cols = ["opportunity_id", "sales_agent", "manager", "regional_office", "product",
            "account", "deal_stage", "conversion_probability", "priority"]
    scored = open_deals[cols].sort_values("conversion_probability", ascending=False)
    scored.to_csv("outputs/scored_leads.csv", index=False)
    scored.to_csv("dashboard/scored_leads.csv", index=False)
    print(f"Best model: {best_name}. Scored {len(scored)} open deals -> outputs/scored_leads.csv")


if __name__ == "__main__":
    main()
