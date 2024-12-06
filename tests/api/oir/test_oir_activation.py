from . import is_client_response_successful
from . import CONSTRAINT_MANAGEMENT_SCOPE_VALUE
from . import UsspClient, DssClient
from . import UsspFlighPlanMocks as FLIGHT_PLAN_MOCKS


class TestClassOirActivation:

    def __get_ussp_client(self) -> UsspClient:
        return UsspClient(
            is_mocked=False, request_scope=CONSTRAINT_MANAGEMENT_SCOPE_VALUE
        )

    def __get_dss_client(self) -> DssClient:
        return DssClient(request_scope=CONSTRAINT_MANAGEMENT_SCOPE_VALUE)

    def test_setup(self, ussp_client: UsspClient) -> None:
        # TODO: create flight plan with accepted state
        ussp_client.put_oir(
            FLIGHT_PLAN_MOCKS.FLIGHT_PLAN_ID,
            FLIGHT_PLAN_MOCKS.USSP_PUT_FLIGHT_PLAN_ACCEPTED_STATE_REQUEST_BODY,
        )

    def test_case_oir_activation(self) -> None:
        ussp_client = self.__get_ussp_client()
        dss_client = self.__get_dss_client()

        self.test_setup(ussp_client)

        get_oir_dss_response = dss_client.get_oir_by_id(
            FLIGHT_PLAN_MOCKS.FLIGHT_PLAN_ID
        )

        assert is_client_response_successful(get_oir_dss_response)

        # TODO: update flight plan with activated state
        ussp_client.put_oir(OIR_MOCKS.OIR_ID, OIR_MOCKS.USSP_OIR_INJECTION_REQUEST_BODY)

        # TODO: get oir and check if response matches latest updates
