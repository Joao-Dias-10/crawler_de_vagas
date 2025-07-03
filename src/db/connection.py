from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager
from typing import Generator
from src.utils.config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(bind=engine)

@contextmanager
def conectar_db() -> Generator[Session, None, None]:

    #yield db “entrega” esse objeto para quem chamou dentro do bloco with.  Quando o bloco with termina, o código depois do yield (dentro do finally) roda, ou seja:db.close() fecha a sessão/conexão.
    db = SessionLocal()
    try:
        yield db   
    finally:
        db.close()
