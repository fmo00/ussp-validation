from api.utils.client import UTMClientConfig
from requests import Request


class DssClient(UTMClientConfig):
    def __init__(self, session, base_url):
        super().__init__()
        self.base_url = base_url
        self.session = session

    def _generate_authentication_headers(self, bearer_token):
        return {
            "Authorization": "Bearer" + bearer_token,
        }

    def _request_bearer_token(self, set_env_vars):
        url = self.base_url + "/token"
        params = self._generate_request_bearer_token_parameters(set_env_vars)

        req = Request("GET", url, data={}, params=params, headers=self.session.headers)
        prepped_req = self.session.prepare_request(req)

        try:
            return self.session.send(prepped_req)
        except Exception:
            raise Exception()

    def _generate_request_bearer_token_parameters(self, set_env_vars):
        return {
            "scope": set_env_vars.get("DSS_REQUEST_SCOPE"),
            "intended_audience": set_env_vars.get("DSS_REQUEST_INTENDED_AUDIENCE"),
            "apikey": set_env_vars.get("DSS_API_KEY"),
        }

    def set_authentication_headers(self, set_env_vars):
        bearer_token = self._request_bearer_token(set_env_vars).json()["access_token"]
        self.session.headers.update(
            self._generate_authentication_headers(str(bearer_token))
        )

    def request_get_oir_query(self, oir_id):
        url = self.base_url + f"/dss/v1/operational_intent_references/${oir_id}"

        req = Request("GET", url, data={}, headers={})
        prepped_req = self.session.prepare_request(req)
        try:
            return self.session.send(prepped_req)
        except Exception:
            raise Exception()
