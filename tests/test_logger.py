import logging
from src.utils.logger import default_logger

def test_default_logger_exists():
    assert isinstance(default_logger, logging.Logger)
    assert default_logger.name == "app"

def test_default_logger_level():
    assert default_logger.level == logging.INFO or default_logger.getEffectiveLevel() == logging.DEBUG
