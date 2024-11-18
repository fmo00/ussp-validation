from requests import Session
from requests.exceptions import HTTPError


class ClientSessionConfig:
    session = Session()

    def __init__(self):
        return

    def get_client_session(self) -> Session:
        try:
            return self.session
        except HTTPError:
            raise

    def end_client_session(self) -> None:
        try:
            return self.session.close()

        except HTTPError:
            raise
