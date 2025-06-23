import pytest
from src.preprocessing.limpeza import limpar_vagas

def test_limpar_vagas():
    entrada = [
        {
            "titulo": "  Dev Python  ",
            "empresa": " Google ",
            "localizacao": " SP "
        }
    ]

    saida_esperada = [
        {
            "titulo": "Dev Python",
            "empresa": "Google",
            "localizacao": "SP"
        }
    ]

    assert limpar_vagas(entrada) == saida_esperada
