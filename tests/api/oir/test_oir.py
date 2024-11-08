from api.utils.ussp_client import UsspClient
from api.utils.dss_client import DssClient
from api.utils.client import UTMClientConfig

class TestClassOirInjection:
    def _ussp_client(self, base_url):
        client_config = UTMClientConfig()
        session = client_config.get_client_session()
        return UsspClient(session, base_url)
    
    def _dss_client(self, base_url):
        client_config = UTMClientConfig()
        session = client_config.get_client_session()
        return DssClient(session, base_url)

    def _validate_oir(self):
        #def _validate_oir(self, requested_oir, dss_oir, ussp_oir):
        #TODO
        assert True 

    def test_case_isolated_oir(self, set_env_vars):
        ussp_url =  set_env_vars.get("USSP_URL")
        dss_url = set_env_vars.get("DSS_URL")

        response = self._ussp_client(ussp_url).request_put_oir(request_body={})

        if response.status_code != 201:
            assert False
        
        dss_response = self._dss_client(dss_url).request_get_oir_query('123')

        self._validate_oir(self)
       
            
    def test_case_conflicted_oir_constraint(self, set_env_vars):
        #TODO
        return
    
    def test_case_conflicted_oir(self, set_env_vars):
        #TODO
        return