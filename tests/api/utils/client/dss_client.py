from os import _Environ
from api.utils.client.utm_client import UTMClientConfig
from requests import Request, Response, Session


class DssClient(UTMClientConfig):
    def __init__(self, session: Session, base_url: str):
        super().__init__()
        self.base_url = base_url
        self.session = session

    def _generate_authentication_headers(self, bearer_token: str):
        return {
            "Authorization": "Bearer" + bearer_token,
        }

    def _generate_request_bearer_token_parameters(self, set_env_vars: _Environ[str]):
        return {
            "scope": set_env_vars.get("DSS_REQUEST_SCOPE"),
            "intended_audience": set_env_vars.get("DSS_REQUEST_INTENDED_AUDIENCE"),
            "apikey": set_env_vars.get("DSS_API_KEY"),
        }

    def set_authentication_headers(self, set_env_vars: _Environ[str]) -> None:
        bearer_token = self._request_bearer_token(set_env_vars).json()["access_token"]
        self.session.headers.update(
            self._generate_authentication_headers(str(bearer_token))
        )

    def _request_bearer_token(self, set_env_vars: _Environ[str]) -> Response:
        url = self.base_url + "/token"
        params = self._generate_request_bearer_token_parameters(set_env_vars)

        req = Request("GET", url, data={}, params=params, headers=self.session.headers)
        prepped_req = self.session.prepare_request(req)

        try:
            return self.session.send(prepped_req)
        except Exception:
            raise Exception()

    def request_get_oir_query(self, oir_id: str) -> Response:
        url = self.base_url + f"/dss/v1/operational_intent_references/${oir_id}"

        req = Request("GET", url, data={}, headers={})
        prepped_req = self.session.prepare_request(req)
        try:
            return self.session.send(prepped_req)
        except Exception:
            raise Exception()
