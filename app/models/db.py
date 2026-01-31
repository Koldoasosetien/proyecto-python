# app/models/db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

DATABASE_URL = "sqlite:///biblioteca.db"

engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args={"check_same_thread": False}
)

sessionFactory = sessionmaker(bind=engine)
session = scoped_session(sessionFactory)
