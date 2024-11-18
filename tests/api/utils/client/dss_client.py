from os import environ
from api.utils.client.utm_client import UTMClientConfig
from requests import Request, Response, Session
from . import AuthenticationHeaderBuilder
from api.utils.client.auth_client import AuthenticationClient


class DssClient(UTMClientConfig):
    def __init__(self, session: Session):
        super().__init__()
        self.base_url = environ.get("DSS_URL")
        self.session = session
        self.auth_header_builder = AuthenticationHeaderBuilder(
        is_mocked=False
        )
        self.auth_client = AuthenticationClient(session, is_mocked=False)

    def __get_bearer_token(self) -> Response:
        return self.auth_client.get_bearer_token()

    def __set_authentication_headers(self) -> None:
        bearer_token = self.__get_bearer_token().json()["access_token"]
        auth_header = self.auth_header_builder.build_authentication_headers(
            str(bearer_token)
        )
        self.session.headers.update(auth_header)

    def get_oir_by_id(
        self, oir_id: str
    ) -> Response:
        self.__set_authentication_headers()
        url = self.base_url + f"/dss/v1/operational_intent_references/${oir_id}"

        req = Request("GET", url, data={})
        prepped_req = self.session.prepare_request(req)
        try:
            return self.session.send(prepped_req)
        except Exception as err:
            raise err

    #TODO: implement request body type class
    def put_oir(
        self, oir_id:str, request_body
    ) -> Response:
        self.__set_authentication_headers()
        url = self.base_url + f"/dss/v1/operational_intent_references/{oir_id}"
        
        req = Request("PUT", url, data=request_body)
        prepped_req = self.session.prepare_request(req)
        try:
            return self.session.send(prepped_req)
        except Exception as err:
            raise err