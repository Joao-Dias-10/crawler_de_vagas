from src.db.connection import engine
from src.db.models import Base
from typing import Optional

class DatabaseManager:
    def __init__(self, engine: Optional[engine] = engine):

        self.engine = engine

    def create_table(self) -> None:

        Base.metadata.create_all(bind=self.engine)

