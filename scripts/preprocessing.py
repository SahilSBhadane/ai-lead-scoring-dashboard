import pandas as pd

TARGET = "won"

# Columns that are only known AFTER a deal closes (or are the label itself).
# Keeping any of these in the features leaks the answer into the model.
LEAKY_COLS = ["deal_stage", "close_date", "close_value"]

# Identifiers - unique per row, no predictive meaning
ID_COLS = ["opportunity_id", "account"]

CATEGORICAL = [
    "sales_agent", "product", "series", "sector", "office_location",
    "subsidiary_of", "manager", "regional_office",
]
NUMERIC = [
    "sales_price", "revenue", "employees", "year_established",
    "engage_month", "engage_dayofweek",
]
FEATURES = CATEGORICAL + NUMERIC


def add_features(df):
    df = df.copy()
    engage = pd.to_datetime(df["engage_date"], errors="coerce")
    df["engage_month"] = engage.dt.month
    df["engage_dayofweek"] = engage.dt.dayofweek
    for col in CATEGORICAL:
        df[col] = df[col].fillna("Unknown").astype(str)
    return df


def split_closed_and_open(df):
    """
    Closed deals (Won/Lost) have a known outcome -> used to train and evaluate.
    Open deals (Engaging/Prospecting) have no outcome yet -> these are what we score.
    """
    df = add_features(df)
    closed = df[df["deal_stage"].isin(["Won", "Lost"])].copy()
    closed[TARGET] = (closed["deal_stage"] == "Won").astype(int)
    open_deals = df[df["deal_stage"].isin(["Engaging", "Prospecting"])].copy()
    return closed, open_deals
