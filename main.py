from src.automation.robot import coletar_vagas
from src.preprocessing.limpeza import limpar_vagas
from src.db.connection import conectar_db
from src.db.queries import inserir_vagas_no_banco
from src.utils.logger import default_logger as logger
from src.db.init_db import create_table

def run():
    try:
        logger.info("Criando tabelas se não existirem.")
        create_table()

        logger.info("Iniciando coleta de vagas.")
        vagas_raw = coletar_vagas("Python remoto")

        logger.info("Limpando as vagas coletadas.")
        vagas_limpas = limpar_vagas(vagas_raw)

        logger.info(f"{len(vagas_limpas)} vagas após limpeza.")

        logger.info("Conectando ao banco e inserindo vagas.")
        with conectar_db() as db:
            for vaga in vagas_limpas:
                inserir_vagas_no_banco(db, vaga)

        logger.info("Processo finalizado com sucesso!\n\n")

    except Exception as e:
        logger.error(f"Erro registrado: {e}\n\n", exc_info=True)

if __name__ == "__main__":
    run()
