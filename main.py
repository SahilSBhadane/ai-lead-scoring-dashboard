from scripts.data_merge import load_and_merge_data
from scripts.preprocessing import preprocess_data
from scripts.modeling import train_and_evaluate
from sklearn.model_selection import train_test_split
import pandas as pd
import os


def main():
    print("🔄 Loading and merging data...")
    df = load_and_merge_data()

    print("⚙️  Preprocessing...")
    X, y, _ = preprocess_data(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("🤖 Training models...")
    best_model, reports = train_and_evaluate(X_train, X_test, y_train, y_test)

    print("✅ Saving model predictions...")
    preds = best_model.predict(X_test)

    result_df = X_test.copy()
    result_df['conversion_score'] = preds
    result_df['opportunity_level'] = pd.cut(preds, bins=[0, 0.4, 0.7, 1.0], labels=['Low', 'Medium', 'High'])
    result_df.to_csv("outputs/scored_leads.csv", index=False)

    print("📝 Writing metrics report...")
    with open("outputs/metrics_report.txt", "w") as f:
        for model_name, report in reports.items():
            # Remove model object before writing to file
            clean_report = {k: v for k, v in report.items() if k != 'model'}
            f.write(f"\nModel: {model_name}\n")
            f.write(pd.DataFrame(clean_report, index=[0]).transpose().to_string())
            f.write("\n")

    print("🚀 Done! Check the outputs folder.")


if __name__ == "__main__":
    os.makedirs("outputs", exist_ok=True)
    main()
