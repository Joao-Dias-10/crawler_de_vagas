from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import declarative_base

# Herdar de Base (import do sqlalchemy) transforma a classe normal Python numa classe ORM, com todos os 'facilitadores' do mesmo.
Base = declarative_base()

class VagaEmprego(Base):
    __tablename__ = 'vagas_emprego'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(Text, nullable=False)
    empresa: str = Column(Text)
    localizacao: str = Column(Text)
    url: str = Column(Text, nullable=False, unique=True)

    # O método __repr__ define como o objeto aparece quando você imprime ele. Ajuda para debug e logs.
    def __repr__(self) -> str:
        return f"VagaEmprego(id={self.id}, titulo={self.titulo}, empresa={self.empresa}, localizacao={self.localizacao}, url={self.url})"
