from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class VagaEmprego(Base):
    __tablename__ = 'vagas_emprego'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(Text, nullable=False)
    empresa: str = Column(Text)
    localizacao: str = Column(Text)
    url: str = Column(Text, nullable=False, unique=True)

    def __repr__(self) -> str:
        return f"VagaEmprego(id={self.id}, titulo={self.titulo}, empresa={self.empresa}, localizacao={self.localizacao}, url={self.url})"
