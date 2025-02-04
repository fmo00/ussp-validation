from os import environ
from requests import Request, Response
from utils.client.client_session_config import ClientSessionConfig
from . import AuthenticationHeaderBuilder
from . import GET_TOKEN_PATH


class AuthenticationClient:
    def __init__(self, is_mocked: bool, scope: str, client_type: str):
        self.base_url: str = environ.get("KONG_GATEWAY_API_URL")
        self.session = ClientSessionConfig().get_client_session()
        self.auth_header_builder = AuthenticationHeaderBuilder(
            is_mocked, scope, client_type
        )

    def get_bearer_token(self) -> Response:
        url = self.base_url + GET_TOKEN_PATH
        params = self.auth_header_builder.get_request_bearer_token_parameters()

        req = Request("GET", url, data={}, params=params, headers=self.session.headers)
        prepped_req = self.session.prepare_request(req)

        try:
            response = self.session.send(prepped_req)
            return response
        except Exception as err:
            raise err
