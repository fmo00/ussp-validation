from api.utils.client.utm_client import UTMClientConfig
from os import _Environ
from requests import Request, Response, Session
from . import AuthenticationHeaderBuilder
from . import GET_TOKEN_PATH


class AuthenticationClient(UTMClientConfig):
    def __init__(self, session: Session, set_env_vars: _Environ[str]):
        super().__init__()
        self.base_url = set_env_vars.get("KONG_URL")
        self.session = session
        self.auth_header_builder = AuthenticationHeaderBuilder()

    def request_bearer_token(self, set_env_vars: _Environ[str]) -> Response:
        url = self.base_url + GET_TOKEN_PATH
        params = self.auth_header_builder.build_request_bearer_token_parameters(
            set_env_vars
        )

        req = Request("GET", url, data={}, params=params, headers=self.session.headers)
        prepped_req = self.session.prepare_request(req)

        try:
            return self.session.send(prepped_req)
        except Exception:
            raise Exception()
