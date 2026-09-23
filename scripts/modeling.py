import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, average_precision_score, roc_auc_score
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from xgboost import XGBClassifier

from scripts.preprocessing import CATEGORICAL, NUMERIC


def _preprocessor(scale_numeric):
    num_steps = [("impute", SimpleImputer(strategy="median"))]
    if scale_numeric:
        num_steps.append(("scale", StandardScaler()))
    return ColumnTransformer([
        ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL),
        ("num", Pipeline(num_steps), NUMERIC),
    ])


def build_models():
    return {
        "Baseline (majority class)": Pipeline([
            ("prep", _preprocessor(scale_numeric=False)),
            ("clf", DummyClassifier(strategy="prior")),
        ]),
        "Logistic Regression": Pipeline([
            ("prep", _preprocessor(scale_numeric=True)),
            ("clf", LogisticRegression(max_iter=2000, class_weight="balanced")),
        ]),
        "XGBoost": Pipeline([
            ("prep", _preprocessor(scale_numeric=False)),
            ("clf", XGBClassifier(
                n_estimators=300, max_depth=4, learning_rate=0.05,
                subsample=0.8, colsample_bytree=0.8,
                eval_metric="logloss", random_state=42,
            )),
        ]),
    }


def train_and_evaluate(X_train, X_test, y_train, y_test):
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    results, best_name, best_auc = {}, None, -np.inf

    for name, model in build_models().items():
        cv_auc = cross_val_score(model, X_train, y_train, cv=cv, scoring="roc_auc")
        model.fit(X_train, y_train)
        proba = model.predict_proba(X_test)[:, 1]
        results[name] = {
            "model": model,
            "cv_roc_auc_mean": cv_auc.mean(),
            "cv_roc_auc_std": cv_auc.std(),
            "test_roc_auc": roc_auc_score(y_test, proba),
            "test_pr_auc": average_precision_score(y_test, proba),
            "test_accuracy": accuracy_score(y_test, (proba >= 0.5).astype(int)),
        }
        print(f"{name:28s} CV ROC-AUC {cv_auc.mean():.3f} ± {cv_auc.std():.3f} | "
              f"test ROC-AUC {results[name]['test_roc_auc']:.3f}")
        if not name.startswith("Baseline") and results[name]["cv_roc_auc_mean"] > best_auc:
            best_name, best_auc = name, results[name]["cv_roc_auc_mean"]

    return best_name, results
