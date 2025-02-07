from os import environ
from constant.authentication import AuthenticationConstant
from adapter.auth_service.auth_audience_dict import audience_dictionary


class AuthenticationHeaderBuilder:
    def __init__(self, scope: str, client_type: bool):
        self.bearer_token_req_params = self.__build_request_bearer_token_parameters(scope, client_type
        )

    def __build_request_bearer_token_parameters(
        self, scope: str, client_type: str
    ) -> str:
        return self.__build_token_request_query_parameters(scope, client_type)

    def __build_token_audience(self, client_type: str) -> str:
        return audience_dictionary.get(client_type)

    def __build_token_request_query_parameters(
        self, scope: str, client_type: str
    ) -> dict:
        #TODO: use import to clean this 
        return {
            AuthenticationConstant.QUERY_PARAM_SCOPE_NAME: scope,
            AuthenticationConstant.QUERY_PARAM_INTENDED_AUDIENCE_NAME: self.__build_token_audience(
                client_type
            ),
            AuthenticationConstant.QUERY_PARAM_API_KEY_NAME: environ.get("DSS_API_KEY"),
        }

    def get_request_bearer_token_parameters(self) -> str:
        return self.bearer_token_req_params