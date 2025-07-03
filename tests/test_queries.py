from unittest.mock import MagicMock
from src.db.queries import VagaDBManager 
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

    # Instanciando o VagaDBManager
    vaga_db_manager = VagaDBManager(mock_db)

    # Chama o método para inserir a vaga no banco
    vaga_db_manager.inserir_vagas_no_banco(vaga)

    # Verifica se o método add foi chamado para adicionar a nova vaga
    mock_db.add.assert_called_once()
    # Verifica se o commit foi chamado uma vez
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

    # Instanciando o VagaDBManager
    vaga_db_manager = VagaDBManager(mock_db)

    # Chama o método para tentar inserir a vaga no banco
    vaga_db_manager.inserir_vagas_no_banco(vaga)

    # Verifica se o método add **não** foi chamado, pois a vaga já existe
    mock_db.add.assert_not_called()
    # Verifica se o commit **não** foi chamado
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

    # Instanciando o VagaDBManager
    vaga_db_manager = VagaDBManager(mock_db)

    # Chama a função para verificar se a vaga existe
    resultado = vaga_db_manager.vaga_existe("Dev", "Empresa", "SP")

    # Verifica se o resultado é True, pois a vaga foi encontrada
    assert resultado is True


def test_vaga_existe_false():
    mock_db = MagicMock()
    mock_db.query().filter().first.return_value = None

    # Instanciando o VagaDBManager
    vaga_db_manager = VagaDBManager(mock_db)

    # Chama a função para verificar se a vaga existe
    resultado = vaga_db_manager.vaga_existe("Dev", "Empresa", "SP")

    # Verifica se o resultado é False, pois a vaga não foi encontrada
    assert resultado is False
