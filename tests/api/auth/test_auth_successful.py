from . import UTMClientConfig
from . import UsspClient
from . import _is_client_response_not_found
from . import OirMocks


class TestClassUssSuccessAuthentication:
    def __get_ussp_client(self) -> UsspClient:
        session = UTMClientConfig().get_client_session()
        return UsspClient(session, is_mocked=False)

    def test_case_bearer_token_validation(self) -> None:
        ussp_client = self.__get_ussp_client()

        response = ussp_client.get_oir_by_id(OirMocks.INVALID_OIR_ID)
        if _is_client_response_not_found(response):
            assert True
            return

        assert False
