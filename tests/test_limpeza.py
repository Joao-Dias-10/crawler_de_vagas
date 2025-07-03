from src.preprocessing.limpeza import VagaLimpeza 

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

    # Instancia a classe VagaLimpeza
    limpador = VagaLimpeza(entrada)  # Passando a entrada para a classe
    resultado = limpador.limpar_vagas()  # Chamando o método de limpeza

    assert resultado == saida_esperada
