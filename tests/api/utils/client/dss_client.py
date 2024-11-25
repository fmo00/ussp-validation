from os import environ
from requests import Request, Response
from api.utils.client.client_session_config import ClientSessionConfig
from api.utils.client.auth_client import AuthenticationClient
from api.dto.dss.oir.request.oir_injection_request_body import OirInjectionRequestDto
from . import DSS_CLIENT_TYPE


class DssClient:
    def __init__(self, request_scope: str):
        self.base_url = environ.get("DSS_URL")
        self.session = ClientSessionConfig().get_client_session()
        self.auth_client = AuthenticationClient(
            is_mocked=False, scope=request_scope, client_type=DSS_CLIENT_TYPE
        )

    def __get_bearer_token(self) -> Response:
        return self.auth_client.get_bearer_token()

    def __set_authentication_headers(self) -> None:
        bearer_token = self.__get_bearer_token().json()["access_token"]
        self.session.headers.update({"Authorization": "Bearer" + str(bearer_token)})

    def get_oir_by_id(self, oir_id: str) -> Response:
        self.__set_authentication_headers()
        url = self.base_url + f"/dss/v1/operational_intent_references/${oir_id}"

        req = Request("GET", url, data={})
        prepped_req = self.session.prepare_request(req)
        try:
            return self.session.send(prepped_req)
        except Exception as err:
            raise err

    def put_oir(self, oir_id: str, request_body:OirInjectionRequestDto) -> Response:
        self.__set_authentication_headers()
        url = self.base_url + f"/dss/v1/operational_intent_references/{oir_id}"

        req = Request("PUT", url, data=request_body)
        prepped_req = self.session.prepare_request(req)
        try:
            return self.session.send(prepped_req)
        except Exception as err:
            raise err
