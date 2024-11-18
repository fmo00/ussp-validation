from os import _Environ
from . import UTMClientConfig
from . import UsspClient
from . import _is_client_response_successful
from . import OirMocks


class TestClassUssSuccessAuthentication:
    def __get_ussp_client(self, set_env_vars: _Environ[str]) -> UsspClient:
        session = UTMClientConfig().get_client_session()
        return UsspClient(session, set_env_vars, is_mocked=False)

    def test_case_bearer_token_validation(self, set_env_vars: _Environ[str]) -> None:
        ussp_client = self.__get_ussp_client(set_env_vars)

        response = ussp_client.request_get_oir(OirMocks.OIR_ID)
        if _is_client_response_successful(response):
            assert True

        assert False
