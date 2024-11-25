from . import UsspClient
from . import is_client_response_not_found
from . import OirMocks


class TestClassUssSuccessAuthentication:
    def __get_ussp_client(self) -> UsspClient:
        #TODO: create constant for request scope types
        return UsspClient(is_mocked=False, request_scope="constraint")

    def test_case_bearer_token_validation(self) -> None:
        ussp_client = self.__get_ussp_client()

        response = ussp_client.get_oir_by_id(OirMocks.INVALID_OIR_ID)

        assert is_client_response_not_found(response)
