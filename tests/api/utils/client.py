import requests
from requests.exceptions import HTTPError

class UTMClientConfig:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_client_session(self):
        try:
            return requests.Session()
        except HTTPError:
            raise
       