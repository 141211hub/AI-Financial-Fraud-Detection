import joblib
import shap
import pandas as pd
from pathlib import Path

# ---------------- Load Model ---------------- #

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "saved_models" / "xgboost_model.pkl"

model = joblib.load(MODEL_PATH)

# ---------------- SHAP Explainer ---------------- #

explainer = shap.TreeExplainer(model)


def explain_prediction(data):
    """
    Returns SHAP explanation sorted by feature importance.
    """

    df = pd.DataFrame([data])

    shap_values = explainer(df)

    values = shap_values.values[0]

    explanation = []

    for feature, value in zip(df.columns, values):

        explanation.append(
            {
                "feature": feature,
                "impact": float(value)
            }
        )

    explanation.sort(
        key=lambda x: abs(x["impact"]),
        reverse=True
    )

    return explanation