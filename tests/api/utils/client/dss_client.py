from os import _Environ
from api.utils.client.utm_client import UTMClientConfig
from requests import Request, Response, Session
from . import AuthenticationHeaderBuilder
from api.utils.client.auth_client import AuthenticationClient


class DssClient(UTMClientConfig):
    def __init__(self, session: Session, set_env_vars: _Environ[str]):
        super().__init__()
        self.base_url = set_env_vars.get("DSS_URL")
        self.session = session
        self.auth_header_builder = AuthenticationHeaderBuilder(
            set_env_vars, is_mocked=False
        )
        self.auth_client = AuthenticationClient(session, set_env_vars, is_mocked=False)

    def __get_bearer_token(self, set_env_vars: _Environ[str]) -> Response:
        return self.auth_client.get_bearer_token(set_env_vars)

    def __set_authentication_headers(self, set_env_vars: _Environ[str]) -> None:
        bearer_token = self.__get_bearer_token(set_env_vars).json()["access_token"]
        auth_header = self.auth_header_builder.build_authentication_headers(
            str(bearer_token)
        )
        self.session.headers.update(auth_header)

    def get_oir_by_id(
        self, set_env_vars: _Environ[str], oir_id: str
    ) -> Response:
        self.__set_authentication_headers(set_env_vars)
        url = self.base_url + f"/dss/v1/operational_intent_references/${oir_id}"

        req = Request("GET", url, data={})
        prepped_req = self.session.prepare_request(req)
        try:
            return self.session.send(prepped_req)
        except Exception as err:
            raise err

    #TODO: implement request body type class
    def put_oir(
        self, set_env_vars: _Environ[str], oir_id:str, request_body
    ) -> Response:
        self.__set_authentication_headers(set_env_vars)
        url = self.base_url + f"/dss/v1/operational_intent_references/{oir_id}"
        
        req = Request("PUT", url, data=request_body)
        prepped_req = self.session.prepare_request(req)
        try:
            return self.session.send(prepped_req)
        except Exception as err:
            raise err