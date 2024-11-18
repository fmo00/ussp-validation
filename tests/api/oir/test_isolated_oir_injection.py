from os import _Environ
from . import UsspClient, DssClient, UTMClientConfig
from . import OirMocks as OIR_MOCKS
from . import _is_client_response_successful


class TestClassIsolatedOirInjection:

    def __get_ussp_client(self, set_env_vars: _Environ[str]) -> UsspClient:
        session = UTMClientConfig().get_client_session()
        return UsspClient(session, set_env_vars)

    def __get_dss_client(self, set_env_vars: _Environ[str]) -> DssClient:
        session = UTMClientConfig().get_client_session()
        client = DssClient(session, set_env_vars)
        return client

    def __validate_oir_object(self, dss_oir, ussp_oir) -> None:
        ussp_oir_ref = ussp_oir["operational_intent"]["reference"]
        dss_oir_ref = dss_oir["operational_intent_reference"]

        assert ussp_oir_ref is dss_oir_ref

    def test_case_isolated_oir(self, set_env_vars: _Environ[str]) -> None:
        ussp_client = self.__get_ussp_client(set_env_vars)
        dss_client = self.__get_dss_client(set_env_vars)

        response = ussp_client.request_put_oir(
            OIR_MOCKS.OIR_ID, OIR_MOCKS.USSP_OIR_INJECTION_REQUEST_BODY
        )

        if not _is_client_response_successful(response):
            assert False

        dss_oir = dss_client.request_get_oir_query(OIR_MOCKS.OIR_ID)
        ussp_oir = ussp_client.request_get_oir(OIR_MOCKS.OIR_ID)

        if _is_client_response_successful(dss_oir) and _is_client_response_successful(
            ussp_oir
        ):
            self.__validate_oir_object(
                dss_oir.json(),
                ussp_oir.json(),
            )

        assert False
