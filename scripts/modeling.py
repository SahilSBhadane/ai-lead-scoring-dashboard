from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np


def train_and_evaluate(X_train, X_test, y_train, y_test):
    print("🚀 Training and evaluating models...")

    models = {
        'Linear Regression': LinearRegression(),
        'Random Forest': RandomForestRegressor(random_state=42)
    }

    results = {}
    best_model = None
    best_score = -np.inf  # We want highest R^2

    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)

        rmse = np.sqrt(mean_squared_error(y_test, preds))
        r2 = r2_score(y_test, preds)

        results[name] = {'model': model, 'RMSE': rmse, 'R^2': r2}
        print(f"📊 {name} — RMSE: {rmse:.2f}, R^2: {r2:.2f}")

        if r2 > best_score:
            best_score = r2
            best_model = model

    return best_model, results
