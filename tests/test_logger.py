import logging
from src.utils.logger import LoggerConfig

def test_logger_exists():
    logger = LoggerConfig(logger_name="test-logger").configurar()
    assert isinstance(logger, logging.Logger)
    assert logger.name == "test-logger"

def test_logger_level():
    logger = LoggerConfig(log_level="DEBUG", logger_name="test-logger").configurar()
    assert logger.level == logging.DEBUG or logger.getEffectiveLevel() == logging.DEBUG
