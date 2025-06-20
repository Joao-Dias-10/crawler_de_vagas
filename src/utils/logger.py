# src/utils/logger.py

import logging
import os

path = './logs'
log_file_path = f"{path}/execucao.log"
os.makedirs(path, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(log_file_path, mode='a', encoding='utf-8')
    ]
)

# Logger fixo com nome padronizado
default_logger = logging.getLogger("app")  # 'app' será o nome que aparece nos logs
