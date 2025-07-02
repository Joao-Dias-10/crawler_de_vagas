from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager
import os
from typing import Generator
from src.utils.config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(bind=engine)

@contextmanager
def conectar_db() -> Generator[Session, None, None]:

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
