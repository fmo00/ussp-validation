from os import _Environ


class AuthenticationHeaderBuilder:
    def __init__(self):
        pass

    # TODO: add return types for this class methods
    def build_request_bearer_token_parameters(self, set_env_vars: _Environ[str]):
        return {
            "scope": set_env_vars.get("DSS_REQUEST_SCOPE"),
            "intended_audience": set_env_vars.get("DSS_REQUEST_INTENDED_AUDIENCE"),
            "apikey": set_env_vars.get("DSS_API_KEY"),
        }

    def build_authentication_headers(self, bearer_token: str):
        return {
            "Authorization": "Bearer" + bearer_token,
        }
