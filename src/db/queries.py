# src/db/queries.py
from src.db.models import VagaEmprego
from sqlalchemy.orm import Session

class VagaDBManager:
    def __init__(self, db: Session):

        self.db = db

    def inserir_vagas_no_banco(self, vaga: dict) -> None:

        if not self.vaga_existe(vaga["titulo"], vaga["empresa"], vaga["localizacao"]):
            nova_vaga = VagaEmprego(
                titulo=vaga["titulo"],
                empresa=vaga["empresa"],
                localizacao=vaga["localizacao"],
                url=vaga["url"]
            )
            self.db.add(nova_vaga)
            self.db.commit()

    def vaga_existe(self, titulo: str, empresa: str, localizacao: str) -> bool:
     
        return self.db.query(VagaEmprego).filter(
            VagaEmprego.titulo == titulo,
            VagaEmprego.empresa == empresa,
            VagaEmprego.localizacao == localizacao
        ).first() is not None
