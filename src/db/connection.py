# src/db/connection.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
import os
from src.utils.configsAll import *

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

@contextmanager
def conectar_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
