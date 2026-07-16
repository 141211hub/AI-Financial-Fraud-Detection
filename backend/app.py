from fastapi import FastAPI

from schemas import Transaction
from predict import predict_transaction
from explain import explain_prediction
from ai.assistant import generate_summary

from database.database import SessionLocal, engine
from database.models import Base
from database.crud import save_prediction
from database.models import Prediction
from report import generate_report
from reports.pdf_report import generate_pdf
from fastapi.responses import FileResponse

app = FastAPI(
    title="AI Financial Fraud Detection API",
    version="1.0"
)

# Create database tables
Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
        "message": "Fraud Detection API Running Successfully"
    }


@app.post("/predict")
def predict(transaction: Transaction):

    transaction_dict = transaction.model_dump()

    prediction, probability = predict_transaction(transaction_dict)

    if prediction == 1:
        result = "Fraud"
    else:
        result = "Genuine"

    probability_percent = round(probability * 100, 2)

    if probability_percent < 30:
        risk = "Low"
    elif probability_percent < 70:
        risk = "Medium"
    else:
        risk = "High"

    # Save prediction to database
    db = SessionLocal()

    save_prediction(
        db=db,
        amount=transaction.Amount,
        prediction=result,
        probability=probability_percent,
        risk=risk
    )

    db.close()

    return {
        "prediction": result,
        "fraud_probability": probability_percent,
        "risk_level": risk
    }


@app.post("/explain")
def explain(transaction: Transaction):

    transaction_dict = transaction.model_dump()

    explanation = explain_prediction(transaction_dict)

    return {
        "top_features": explanation[:10]
    }


@app.post("/assistant")
def assistant(data: dict):

    summary = generate_summary(
        transaction=data["transaction"],
        prediction=data["prediction"],
        probability=data["fraud_probability"],
        risk=data["risk_level"]
    )

    return {
        "summary": summary
    }

@app.get("/history")
def get_history():

    db = SessionLocal()

    history = db.query(Prediction).order_by(
        Prediction.id.desc()
    ).all()

    db.close()

    return history
@app.post("/generate-report")
def create_report(data: dict):

    filename = generate_report(

        prediction=data["prediction"],

        probability=data["fraud_probability"],

        risk=data["risk_level"],

        transaction=data["transaction"],

        explanation=data["explanation"],

        summary=data["summary"]

    )

    return {

        "report": filename

    }
@app.post("/report")
def report(data: dict):

    filename = "investigation_report.pdf"

    generate_pdf(
        filename=filename,
        transaction=data["transaction"],
        prediction=data["prediction"],
        probability=data["fraud_probability"],
        risk=data["risk_level"],
        summary=data["summary"]
    )

    return FileResponse(
        filename,
        media_type="application/pdf",
        filename="SecureBank_AI_Report.pdf"
    )