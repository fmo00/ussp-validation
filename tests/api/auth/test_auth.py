from os import _Environ
from . import AuthenticationClient
from . import UTMClientConfig


class TestClassUssAuthentication:
    def __auth_client(self, set_env_vars) -> AuthenticationClient:
        client_config = UTMClientConfig()
        session = client_config.get_client_session()
        return AuthenticationClient(session, set_env_vars)

    def test_case_bearer_token_validation(self, set_env_vars: _Environ[str]) -> None:
        self.__auth_client(set_env_vars).request_bearer_token(set_env_vars)
        assert False
