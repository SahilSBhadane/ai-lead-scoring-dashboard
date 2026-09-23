import pandas as pd


def load_and_merge_data(data_dir="data"):
    """Load the 4 CRM tables and join them onto the sales pipeline."""
    pipeline = pd.read_csv(f"{data_dir}/sales_pipeline.csv")
    accounts = pd.read_csv(f"{data_dir}/accounts.csv")
    products = pd.read_csv(f"{data_dir}/products.csv")
    teams = pd.read_csv(f"{data_dir}/sales_teams.csv")

    # Fix typos in the source column names
    accounts = accounts.rename(columns={"yeear_established": "year_established"})
    products = products.rename(columns={"saales_price": "sales_price"})
    teams = teams.rename(columns={"manager'": "manager"})

    # Product names differ between tables in the raw data ("GTXPro" vs "GTX Pro")
    pipeline["product"] = pipeline["product"].replace({"GTXPro": "GTX Pro"})

    df = (
        pipeline.merge(accounts, on="account", how="left")
        .merge(products, on="product", how="left")
        .merge(teams, on="sales_agent", how="left")
    )
    return df
