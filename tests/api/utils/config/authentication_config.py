from os import environ
from api.constants.auth import QUERY_PARAM_API_KEY_NAME, QUERY_PARAM_INTENDED_AUDIENCE_NAME, QUERY_PARAM_SCOPE_NAME
from . import AuthenticationMocks


class AuthenticationHeaderBuilder:
    def __init__(self, is_mocked: bool):
        self.bearer_token_req_params = self.__build_request_bearer_token_parameters(
            is_mocked
        )

    # TODO: add return types for this class methods
    def __build_request_bearer_token_parameters(self, is_mocked: bool) -> str:
        return (
            self.__build_mocked_token_request_query_parameters()
            if is_mocked
            else self.__build_valid_request_bearer_token_parameters()
        )

    def __build_mocked_token_request_query_parameters(self) -> str:
        return AuthenticationMocks.INVALID_TOKEN_REQUEST_PARAMETER_STR

    def __build_valid_request_bearer_token_parameters(self) -> str:
        return (
            QUERY_PARAM_SCOPE_NAME
            + environ.get("DSS_REQUEST_SCOPE")
            + QUERY_PARAM_INTENDED_AUDIENCE_NAME
            + environ.get("DSS_REQUEST_INTENDED_AUDIENCE")
            + QUERY_PARAM_API_KEY_NAME
            + environ.get("DSS_API_KEY"),
        )

    def get_request_bearer_token_parameters(self):
        return self.bearer_token_req_params

    def build_authentication_headers(self, bearer_token: str):
        return {
            "Authorization": "Bearer" + bearer_token,
        }
