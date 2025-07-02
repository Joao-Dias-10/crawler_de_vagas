import logging
import os
from typing import Optional

class LoggerConfig:
    def __init__(self, log_path: Optional[str] = './logs', log_filename: str = 'execucao.log', log_level: str = 'INFO'):
        self.log_path = log_path
        self.log_filename = log_filename
        self.log_level = log_level.upper()

        # Garantir que o diretório de logs exista
        os.makedirs(self.log_path, exist_ok=True)

        # Configuração do logging
        self.logger = logging.getLogger("app")
        self.logger.setLevel(self.log_level)

        # Formatação do log
        log_format = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
        formatter = logging.Formatter(log_format)

        # Handler para escrever no console
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        # Handler para escrever no arquivo
        log_file_path = os.path.join(self.log_path, self.log_filename)
        file_handler = logging.FileHandler(log_file_path, mode='a', encoding='utf-8')
        file_handler.setFormatter(formatter)

        # Adicionar apenas o handler do console, se ele não existir já
        if not self.logger.handlers:  # Verifica se já há handlers configurados
            self.logger.addHandler(stream_handler)
            self.logger.addHandler(file_handler)

    def get_logger(self) -> logging.Logger:
        return self.logger

# Crie a instância default_logger para que ela possa ser importada
default_logger = LoggerConfig().get_logger()
