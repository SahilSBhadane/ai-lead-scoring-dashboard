import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

def preprocess_data(df):
    print("⚙️  Preprocessing...")

    # Drop rows with missing target (you don’t have 'converted', so create a target!)
    df = df.dropna(subset=['close_value'])  # Using 'close_value' as proxy target
    # Drop rows with missing values (quick fix)
    df = df.dropna()

    # Target variable: assume deal is won if close_value > 0
    df['converted'] = df['close_value'].apply(lambda x: 1 if x > 0 else 0)

    # Drop unnecessary columns
    df = df.drop(['opportunity_id', 'account', 'engage_date', 'close_date', 'close_value'], axis=1)

    # Separate features and target
    X = df.drop('converted', axis=1)
    y = df['converted']

    # One-hot encode categorical variables
    X_encoded = pd.get_dummies(X, drop_first=True)

    return X_encoded, y, None  # no label encoder used
