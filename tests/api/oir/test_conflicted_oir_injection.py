from os import _Environ
from . import UsspClient, DssClient, UTMClientConfig
from . import OirMocks as OIR_MOCKS
from . import _is_client_response_not_found, _is_client_response_conflict


class TestClassConflictedOirInjection:

    def __get_ussp_client(self, set_env_vars: _Environ[str]) -> UsspClient:
        session = UTMClientConfig().get_client_session()
        return UsspClient(session, set_env_vars)

    def __get_dss_client(self, set_env_vars: _Environ[str]) -> DssClient:
        session = UTMClientConfig().get_client_session()
        client = DssClient(session, set_env_vars)
        return client
    
    def test_setup(self, dss_client: DssClient, set_env_vars) -> None:
        dss_client.put_oir(set_env_vars,OIR_MOCKS.OIR_ID,OIR_MOCKS.USSP_OIR_INJECTION_REQUEST_BODY
        )

    def test_case_conflicted_oir(self, set_env_vars: _Environ[str]) -> None:
        ussp_client = self.__get_ussp_client(set_env_vars)
        dss_client = self.__get_dss_client(set_env_vars)

        self.test_setup(dss_client,set_env_vars)

        create_oir_ussp_response = ussp_client.put_oir(
            OIR_MOCKS.OIR_ID, OIR_MOCKS.USSP_OIR_INJECTION_REQUEST_BODY
        )

        if _is_client_response_conflict(create_oir_ussp_response):
            assert True

        get_oir_dss_response = dss_client.get_oir_by_id(set_env_vars,
            OIR_MOCKS.OIR_ID
        )

        if _is_client_response_not_found(get_oir_dss_response):
            assert True
            return 
      
        assert False
