from src.db.connection import engine
from src.db.models import Base

def create_table():
    Base.metadata.create_all(bind=engine)