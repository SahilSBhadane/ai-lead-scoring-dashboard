import pandas as pd

def load_and_merge_data():
    print("🔄 Loading and merging data...")

    pipeline = pd.read_csv("data/sales_pipeline.csv")
    accounts = pd.read_csv("data/accounts.csv")
    products = pd.read_csv("data/products.csv")
    teams = pd.read_csv("data/sales_teams.csv")

    # Fixing typos in column names
    accounts.rename(columns={'yeear_established': 'year_established'}, inplace=True)
    products.rename(columns={'saales_price': 'sales_price'}, inplace=True)
    teams.rename(columns={"manager'": "manager"}, inplace=True)

    # Merge
    df = pipeline.merge(accounts, on='account', how='left')
    df = df.merge(products, on='product', how='left')
    df = df.merge(teams, on='sales_agent', how='left')

    return df