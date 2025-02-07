from os import environ
from requests import Request, Response, Session

#TODO: use import for better readability
#TODO: add logger
from constant.authentication import AuthenticationConstant
from auth_header_builder import AuthenticationHeaderBuilder

class AuthenticationServiceAdapter:

    def __init__(self):
        self.base_url: str = environ.get("KONG_GATEWAY_API_URL")
        self.session = Session()
        self.auth_header_builder = AuthenticationHeaderBuilder()

    def get_bearer_token(self) -> Response:
        url = self.base_url + AuthenticationConstant.GET_TOKEN_URL_PATH
        params = self.auth_header_builder.get_request_bearer_token_parameters()

        req = Request("GET", url, data={}, params=params, headers=self.session.headers)
        prepped_req = self.session.prepare_request(req)

        try:
            return self.session.send(prepped_req)
        except Exception as err:
            raise err