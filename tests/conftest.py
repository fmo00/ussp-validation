import pytest
import os
from dotenv import load_dotenv

@pytest.fixture(autouse=True)
def set_env_vars(monkeypatch):
    load_dotenv() 

    for key, value in os.environ.items():
        monkeypatch.setenv(key, value)

    return os.environ