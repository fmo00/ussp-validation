from requests import Request, Response
from os import environ
from api.utils.client.client_session_config import ClientSessionConfig
from api.utils.client.auth_client import AuthenticationClient
from . import USSP_CLIENT_TYPE


class UsspClient:
    def __init__(self, is_mocked: bool, request_scope: str):
        self.base_url = environ.get("USSP_URL")
        self.session = ClientSessionConfig().get_client_session()
        self.auth_client = AuthenticationClient(
            is_mocked, scope=request_scope, client_type=USSP_CLIENT_TYPE
        )

    def __get_bearer_token(self) -> Response:
        return self.auth_client.get_bearer_token()

    def __set_authentication_headers(self) -> None:
        bearer_token = self.__get_bearer_token().json()["access_token"]
        self.session.headers.update({"Authorization": "Bearer" + str(bearer_token)})

    # TODO: implement request body type
    def put_oir(self, flight_plan_id: str, request_body) -> Response:
        self.__set_authentication_headers()
        url = self.base_url + f"/flight_planning/v1/flight_plans/{flight_plan_id}"

        req = Request("PUT", url, data=request_body)
        prepped_req = self.session.prepare_request(req)

        try:
            return self.session.send(prepped_req)
        except Exception as err:
            raise err

    def get_oir_by_id(self, oir_id: str) -> Response:
        self.__set_authentication_headers()

        url = self.base_url + f"/uss/v1/operational_intents/${oir_id}"
        req = Request("GET", url)
        prepped_req = self.session.prepare_request(req)

        try:
            return self.session.send(prepped_req)
        except Exception as err:
            raise err
