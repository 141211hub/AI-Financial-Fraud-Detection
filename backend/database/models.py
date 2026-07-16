from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from database.database import Base


class Prediction(Base):

    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)

    amount = Column(Float)

    prediction = Column(String)

    probability = Column(Float)

    risk = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )