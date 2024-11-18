from os import _Environ
from . import AuthenticationMocks


class AuthenticationHeaderBuilder:
    def __init__(self, is_mocked: bool, set_env_vars: _Environ[str]):
        self.bearer_token_req_params = self.__build_request_bearer_token_parameters(
            is_mocked, set_env_vars
        )

    # TODO: add return types for this class methods
    def __build_request_bearer_token_parameters(
        self, is_mocked: bool, set_env_vars: _Environ[str]
    ):
        return (
            self.__build_mocked_request_bearer_token_parameters()
            if is_mocked
            else self.__build_valid_request_bearer_token_parameters(set_env_vars)
        )

    def __build_mocked_request_bearer_token_parameters(self):
        return AuthenticationMocks.INVALID_AUTH_PARAMETERS

    def __build_valid_request_bearer_token_parameters(
        self, set_env_vars: _Environ[str]
    ):
        return {
            "scope": set_env_vars.get("DSS_REQUEST_SCOPE"),
            "intended_audience": set_env_vars.get("DSS_REQUEST_INTENDED_AUDIENCE"),
            "apikey": set_env_vars.get("DSS_API_KEY"),
        }

    def get_request_bearer_token_parameters(self):
        return self.bearer_token_req_params

    def build_authentication_headers(self, bearer_token: str):
        return {
            "Authorization": "Bearer" + bearer_token,
        }
