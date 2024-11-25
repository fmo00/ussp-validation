import os

def pytest_logger_config(logger_config):
   logger_config.add_loggers(['http_logger', 'default'], stdout_level='debug')
   logger_config.set_log_option_default('default')

def pytest_logger_logdirlink():
   return os.path.join(os.path.dirname(__file__), 'logs')