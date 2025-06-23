import pytest
from unittest.mock import MagicMock
from src.db.queries import inserir_vagas_no_banco, vaga_existe
from src.db.models import VagaEmprego


# ------------------------
# Teste da função: inserir_vagas_no_banco
# ------------------------

def test_inserir_vagas_no_banco_nova_vaga():
    mock_db = MagicMock()

    # Simula que vaga_existe retorna False (vaga não existe)
    mock_db.query().filter().first.return_value = None

    vaga = {
        "titulo": "Dev Python",
        "empresa": "Google",
        "localizacao": "SP",
        "url": "https://exemplo.com/vaga"
    }

    inserir_vagas_no_banco(mock_db, vaga)

    mock_db.add.assert_called()
    mock_db.commit.assert_called_once()


def test_inserir_vagas_no_banco_vaga_existente():
    mock_db = MagicMock()

    # Simula que vaga_existe retorna True (vaga já existe)
    mock_db.query().filter().first.return_value = True

    vaga = {
        "titulo": "Dev Python",
        "empresa": "Google",
        "localizacao": "SP",
        "url": "https://exemplo.com/vaga"
    }

    inserir_vagas_no_banco(mock_db, vaga)

    mock_db.add.assert_not_called()
    mock_db.commit.assert_not_called()


# ------------------------
# Teste direto da função: vaga_existe
# ------------------------

def test_vaga_existe_true():
    mock_db = MagicMock()
    mock_db.query().filter().first.return_value = VagaEmprego(
        titulo="Dev",
        empresa="Empresa",
        localizacao="SP",
        url="https://exemplo.com"
    )

    resultado = vaga_existe(mock_db, "Dev", "Empresa", "SP")
    assert resultado is True


def test_vaga_existe_false():
    mock_db = MagicMock()
    mock_db.query().filter().first.return_value = None

    resultado = vaga_existe(mock_db, "Dev", "Empresa", "SP")
    assert resultado is False
