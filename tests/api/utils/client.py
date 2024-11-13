import requests
from requests.exceptions import HTTPError


class UTMClientConfig:
    session = requests.Session()

    def __init__(self):
        return

    def get_client_session(self):
        try:
            return self.session
        except HTTPError:
            raise

    def end_client_session(self):
        try:
            return self.session.close()

        except HTTPError:
            raise
