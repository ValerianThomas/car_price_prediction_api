import pathlib
import logging
from logging.handlers import TimeRotatingFileHandler
import sys


FORMATTER = logging.Formatter(
   "%(asctime)s — %(name)s — %(levelname)s —"
    "%(funcName)s:%(lineno)d — %(message)s"
)

LOG_FILE = Path.cwd() / 'logs' / 'ml_models.log'

def get_console_handler():
  console_handler = logging.StreamHandler(sys.stdout)
  console_handler.setFormatter(FORMATTER)
  return console_handler

def get_file_handler () :
  file_handler = TimeRotatingFileHandler(LOG_FILE, when='midnight')
  file_handler.setFormatter(FORMATTER)
  return file_handler

def get_logger(logger_name):
  logger = logging.getLogger(logger_name)
  logger.SetLevel(logging.DEBUG)
  logger.addHandler(get_console_handler())
  logger.addHandler(get_file_handler())
  logger.propagate = False

  return logger