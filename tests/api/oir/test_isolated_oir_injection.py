from os import environ
from . import UsspClient, DssClient, UTMClientConfig
from . import OirMocks as OIR_MOCKS
from . import is_client_response_successful


class TestClassIsolatedOirInjection:

    def __get_ussp_client(self) -> UsspClient:
        return UsspClient(UTMClientConfig().get_client_session(), is_mocked=False)

    def __get_dss_client(self) -> DssClient:
        return DssClient(UTMClientConfig().get_client_session())
        

    def __validate_oir_object(self, dss_oir, ussp_oir) -> None:
        ussp_oir_ref = ussp_oir["operational_intent"]["reference"]
        dss_oir_ref = dss_oir["operational_intent_reference"]

        assert ussp_oir_ref is dss_oir_ref
        return

    def test_case_isolated_oir(self) -> None:
        ussp_client = self.__get_ussp_client()
        dss_client = self.__get_dss_client()
        
        create_oir_ussp_response = ussp_client.put_oir(
            OIR_MOCKS.OIR_ID, OIR_MOCKS.USSP_OIR_INJECTION_REQUEST_BODY
        )

        if not is_client_response_successful(create_oir_ussp_response):
            assert False 

        dss_oir_response = dss_client.get_oir_by_id(OIR_MOCKS.OIR_ID)
        ussp_oir_response = ussp_client.get_oir_by_id(OIR_MOCKS.OIR_ID)

        if is_client_response_successful(dss_oir_response) and is_client_response_successful(
            ussp_oir_response
        ):
            self.__validate_oir_object(
                dss_oir_response.json(),
                ussp_oir_response.json(),
            )

        assert False
