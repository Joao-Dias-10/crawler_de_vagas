from src.db.models import VagaEmprego
from sqlalchemy.orm import Session

def vaga_existe(db: Session, url: str) -> bool:
    return db.query(VagaEmprego).filter(VagaEmprego.url == url).first() is not None

def inserir_vagas_no_banco(db: Session, vaga: dict):
    if not vaga_existe(db, vaga["url"]):
        nova_vaga = VagaEmprego(
            titulo=vaga["titulo"],
            empresa=vaga["empresa"],
            localizacao=vaga["localizacao"],
            url=vaga["url"]
        )
        db.add(nova_vaga)
        db.commit()
