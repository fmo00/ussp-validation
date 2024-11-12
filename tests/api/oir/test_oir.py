from api.utils.ussp_client import UsspClient
from api.utils.dss_client import DssClient
from api.utils.client import UTMClientConfig
from api.mocks.oir import OirMocks as OIR_MOCKS

class TestClassOirInjection:
    def _ussp_client(self, base_url):
        client_config = UTMClientConfig()
        session = client_config.get_client_session()
        return UsspClient(session, base_url)
    
    def _dss_client(self, base_url):
        client_config = UTMClientConfig()
        session = client_config.get_client_session()
        return DssClient(session, base_url)

    def _validate_oir(self, dss_oir, ussp_oir):
        assert ussp_oir is dss_oir

    def test_case_isolated_oir(self, set_env_vars):
        ussp_url =  set_env_vars.get("USSP_URL")
        dss_url = set_env_vars.get("DSS_URL")
       
        response = self._ussp_client(ussp_url).request_put_oir('123', OIR_MOCKS.USSP_OIR_INJECTION_REQUEST_BODY)

        if response.status_code != 201:
            assert False
        
        dss_oir = self._dss_client(dss_url).request_get_oir_query('123')
        ussp_oir = self._ussp_client(ussp_url).request_get_oir('123')
        self._validate_oir(OIR_MOCKS.USSP_OIR_INJECTION_REQUEST_BODY, dss_oir, ussp_oir)