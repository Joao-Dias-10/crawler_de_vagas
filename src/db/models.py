from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class VagaEmprego(Base):
    __tablename__ = 'vagas_emprego'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(Text, nullable=False)
    empresa = Column(Text)
    localizacao = Column(Text)
    url = Column(Text, nullable=False, unique=True)
