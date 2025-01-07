import logging
import pytest
from dotenv import load_dotenv
from uuid import uuid4
from os import environ

custom_log_format = {
    "host": "%(hostname)s",
    "where": "%(module)s.%(funcName)s",
    "type": "%(levelname)s",
    "stack_trace": "%(exc_text)s",
}

@pytest.fixture(autouse=True)
def load_env():
   load_dotenv() 

def pytest_logger_config(logger_config):
    logger_config.add_loggers(["http_logger", "default"], stdout_level="info")
    logger_config.set_log_option_default("default")

    logger = logging.getLogger("http_logger")
    logger.setLevel(logging.INFO)

@pytest.fixture(autouse=True)
def setup():
   provider_alias = environ.get("PROVIDER_ALIAS")
   test_identifier = uuid4()
   logger = logging.getLogger("http_logger")

   logger.info(f'Execution identifier - {test_identifier}')
   logger.info(f'Provider alias - {provider_alias}')
