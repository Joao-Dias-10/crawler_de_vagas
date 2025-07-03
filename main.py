from src.automation.robot import VagaColetor
from src.preprocessing.limpeza import VagaLimpeza
from src.db.connection import conectar_db
from src.db.queries import VagaDBManager
from src.utils.logger import LoggerConfig
from src.db.init_db import DatabaseManager

def run():
    try:
        # Logger personalizado (nome "app" ou outro se quiser)
        log_config = LoggerConfig(
            log_path='./logs',
            log_filename='execucao.log',
            log_level='DEBUG',
            logger_name='app'  # você pode trocar para outro nome se desejar
        )
        logger = log_config.configurar()

        logger.info("Criando tabelas se não existirem.")
        db_manager = DatabaseManager()
        db_manager.create_table()

        logger.info("Iniciando coleta de vagas.")
        coletor = VagaColetor()
        vagas_raw = coletor.coletar_vagas("Python remoto")

        logger.info("Limpando as vagas coletadas.")
        limpador = VagaLimpeza(vagas_raw)
        vagas_limpas = limpador.limpar_vagas()

        logger.info(f"{len(vagas_limpas)} vagas após limpeza.")

        logger.info("Conectando ao banco e inserindo vagas.")
        with conectar_db() as db:
            vaga_db_manager = VagaDBManager(db)
            for vaga in vagas_limpas:
                vaga_db_manager.inserir_vagas_no_banco(vaga)

        logger.info("Processo finalizado com sucesso!\n\n")

    except Exception as e:
        logger.error(f"Erro registrado: {e}\n\n", exc_info=True)

if __name__ == "__main__":
    run()
