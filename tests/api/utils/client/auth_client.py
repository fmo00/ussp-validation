from api.utils.client.utm_client import UTMClientConfig
from os import environ
from requests import Request, Response, Session
from . import AuthenticationHeaderBuilder
from . import GET_TOKEN_PATH


class AuthenticationClient(UTMClientConfig):
    def __init__(self, session: Session, is_mocked: bool):
        super().__init__()
        self.base_url = environ.get("KONG_URL")
        self.session = session
        self.auth_header_builder = AuthenticationHeaderBuilder(is_mocked)

    def get_bearer_token(self) -> Response:
        url = self.base_url + GET_TOKEN_PATH
        params = self.auth_header_builder.get_request_bearer_token_parameters()

        req = Request("GET", url, data={}, params=params, headers=self.session.headers)
        prepped_req = self.session.prepare_request(req)

        try:
            return self.session.send(prepped_req)
        except Exception:
            raise Exception()
