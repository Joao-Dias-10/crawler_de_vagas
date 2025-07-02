import logging
from src.utils.logger import default_logger

def test_default_logger_exists():
    # Verifica se o logger é uma instância de logging.Logger e se o nome é 'app'
    assert isinstance(default_logger, logging.Logger)
    assert default_logger.name == "app"

def test_default_logger_level():
    # Verifica se o nível de log é INFO ou DEBUG
    assert default_logger.level == logging.INFO or default_logger.getEffectiveLevel() == logging.DEBUG
