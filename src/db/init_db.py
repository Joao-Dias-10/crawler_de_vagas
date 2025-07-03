from sqlalchemy.engine import Engine
from typing import Optional
from src.db.models import Base
from src.db.connection import engine as default_engine

class DatabaseManager:
    def __init__(self, engine: Optional[Engine] = None):
        if engine is None:
            self.engine = default_engine
        else:
            self.engine = engine

    def create_table(self) -> None:
        Base.metadata.create_all(bind=self.engine)
