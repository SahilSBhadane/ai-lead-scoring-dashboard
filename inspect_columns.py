import pandas as pd

# Set your data directory
data_dir = "data/"

# File names
files = {
    "sales_pipeline": "sales_pipeline.csv",
    "accounts": "accounts.csv",
    "products": "products.csv",
    "sales_teams": "sales_teams.csv",
    "metadata": "metadata.csv"
}

# Inspect each file
for name, filename in files.items():
    print(f"\n📄 {name.upper()} ({filename})")
    try:
        df = pd.read_csv(data_dir + filename)
        print(f"➡️  Shape: {df.shape}")
        print(f"➡️  Columns: {df.columns.tolist()}")
        print("🔍 Sample data:")
        print(df.head(3))
    except Exception as e:
        print(f"❌ Could not load {filename}: {e}")
