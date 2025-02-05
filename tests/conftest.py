import logging
import pytest
from dotenv import load_dotenv
from pytest_metadata.plugin import metadata_key  

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
    logger_config.add_loggers(["http_logger", "default"], stdout_level="debug")
    logger_config.set_log_option_default("default")

    logger = logging.getLogger("http_logger")
    logger.setLevel(logging.INFO)

def pytest_html_report_title(report):  
    report.title = "Custom test report WIP"

def pytest_configure(config):  
    config.stash[metadata_key]["Project"] = "ussp-test-suite-kit"
