import joblib
import pandas as pd
from pathlib import Path

# Get project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load model and scaler
MODEL_PATH = BASE_DIR / "saved_models" / "xgboost_model.pkl"
SCALER_PATH = BASE_DIR / "saved_models" / "scaler.pkl"

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


def predict_transaction(transaction_data):
    """
    Predict whether a transaction is Fraud or Genuine
    """

    # Convert dictionary to DataFrame
    df = pd.DataFrame([transaction_data])

    # Scale Amount column
    df["Amount"] = scaler.transform(df[["Amount"]])

    # Prediction
    prediction = int(model.predict(df)[0])

    # Probability
    probability = float(model.predict_proba(df)[0][1])

    return prediction, probability