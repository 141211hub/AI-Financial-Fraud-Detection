from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    Float,
    String
)

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///database/fraud.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


class Prediction(Base):

    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True)

    prediction = Column(String)

    probability = Column(Float)

    risk = Column(String)

    amount = Column(Float)

    time = Column(Float)


Base.metadata.create_all(bind=engine)