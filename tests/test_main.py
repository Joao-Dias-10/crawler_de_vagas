import unittest
from unittest.mock import patch, MagicMock
from main import run

class TestMainRun(unittest.TestCase):

    @patch("main.create_table")
    @patch("main.coletar_vagas")
    @patch("main.limpar_vagas")
    @patch("main.conectar_db")
    @patch("main.inserir_vagas_no_banco")
    @patch("main.logger")
    def test_run_success(
        self, mock_logger, mock_inserir, mock_conectar_db,
        mock_limpar, mock_coletar, mock_create_table
    ):
        # Simula as funções externas
        mock_coletar.return_value = [{"titulo": "Dev Python", "empresa": "Empresa X", "localizacao": "Remoto", "url": "https://url.com"}]
        mock_limpar.return_value = mock_coletar.return_value
        mock_db = MagicMock()
        mock_conectar_db.return_value.__enter__.return_value = mock_db

        # Executa
        run()

        # Verifica chamadas
        mock_create_table.assert_called_once()
        mock_coletar.assert_called_once_with("Python remoto")
        mock_limpar.assert_called_once()
        mock_conectar_db.assert_called_once()
        mock_inserir.assert_called_once_with(mock_db, mock_coletar.return_value[0])
        mock_logger.info.assert_any_call("Processo finalizado com sucesso!\n\n")

    @patch("main.logger")
    @patch("main.create_table", side_effect=Exception("Falha ao criar tabela"))
    def test_run_exception_handling(self, mock_create_table, mock_logger):
        run()
        mock_logger.error.assert_called()
        args, kwargs = mock_logger.error.call_args
        assert "Erro registrado" in args[0]

if __name__ == "__main__":
    unittest.main()
