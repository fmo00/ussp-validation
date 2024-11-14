from os import _Environ
from . import UsspClient, DssClient, UTMClientConfig
from . import OirMocks as OIR_MOCKS
from . import _is_client_response_successful


class TestClassIsolatedOirInjection:
    def _ussp_client(self, base_url: str) -> UsspClient:
        client_config = UTMClientConfig()
        session = client_config.get_client_session()
        return UsspClient(session, base_url)

    def _dss_client(self, base_url: str, set_env_vars: _Environ[str]) -> DssClient:
        client_config = UTMClientConfig()
        session = client_config.get_client_session()
        client = DssClient(session, base_url)
        client.set_authentication_headers(set_env_vars)
        return client

    def _validate_oir_object(self, dss_oir, ussp_oir) -> None:
        ussp_oir_ref = ussp_oir["operational_intent"]["reference"]
        dss_oir_ref = dss_oir["operational_intent_reference"]
        assert ussp_oir_ref is dss_oir_ref

    def test_case_isolated_oir(self, set_env_vars: _Environ[str]) -> None:
        ussp_url = set_env_vars.get("USSP_URL")
        dss_url = set_env_vars.get("DSS_URL")

        response = self._ussp_client(ussp_url).request_put_oir(
            OIR_MOCKS.OIR_ID, OIR_MOCKS.USSP_OIR_INJECTION_REQUEST_BODY
        )

        if not _is_client_response_successful(response):
            assert False

        dss_oir = self._dss_client(dss_url, set_env_vars).request_get_oir_query(
            OIR_MOCKS.OIR_ID
        )
        ussp_oir = self._ussp_client(ussp_url).request_get_oir(OIR_MOCKS.OIR_ID)

        if _is_client_response_successful(dss_oir) and _is_client_response_successful(
            ussp_oir
        ):
            self._validate_oir_object(
                dss_oir.json(),
                ussp_oir.json(),
            )
            return
        assert False
