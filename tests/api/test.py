from os import environ
import logging

logger = logging.getLogger("default")


# TC example
def test_api_url() -> None:
    api_url = environ.get("USSP_URL")
    logger.debug("constructing session thing")
    assert api_url == "https://localhost:8000"
