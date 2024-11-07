#from json_checker import Checker
import pytest
from api.utils.client import UTMClientConfig

class TestClassOirInjection:
    @pytest.fixture
    def ussp_client(set_env_vars):
        return UTMClientConfig(set_env_vars.get("USSP_URL")).get_client_session()

    def test_request_format(self, set_env_vars):
        try:
            #print( self.ussp_client(set_env_vars))
            return self.ussp_client(set_env_vars).get()
        except:
           assert False
       
    assert 100*3 == 200
        
       
            
