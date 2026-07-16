from database.models import Prediction


def save_prediction(
    db,
    amount,
    prediction,
    probability,
    risk
):

    record = Prediction(

        amount=amount,

        prediction=prediction,

        probability=probability,

        risk=risk

    )

    db.add(record)

    db.commit()

    db.refresh(record)

    return record