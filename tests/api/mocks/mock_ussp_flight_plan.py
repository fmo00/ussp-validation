from api.dto.flight_plan.flight_plan_request import FlightPlanInjectionDto
from . import (
    usage_state_switcher,
    uas_state_switcher,
    flight_plan_status_switcher,
    planning_result_switcher,
    includes_advisories_switcher,
)
from . import VolumeMocks
from . import FlightPlanMocks

from uuid import uuid4


class UsspFlighPlanMocks:
    FLIGHT_PLAN_ID: str = "f4959f12-1fa0-41cc-931f-d66866847563"

    USSP_PUT_FLIGHT_PLAN_REQUEST_BODY: FlightPlanInjectionDto = {
        "flight_plan": {
            "basic_information": {
                "usage_state": usage_state_switcher["PLANNED"],
                "uas_state": uas_state_switcher["NOMINAL"],
                "area": [VolumeMocks.VOLUME_4D],
            },
            "astm_f3548_21": FlightPlanMocks.ASTM_F3548_21_OP_INTENT,
            "uspace_flight_authorisation": FlightPlanMocks.USPACE_FLIGHT_AUTH_DATA,
        },
        "execution_style": "IfAllowed",
        "request_id": uuid4(),
    }

    USSP_PUT_FLIGHT_PLAN_RESPONSE = {
        "planning_result": planning_result_switcher["COMPLETED"],
        "notes": "Requested flight intersected operational intent c036326c-c97b-4926-bf9f-c60dc83d2b57",
        "flight_plan_status": flight_plan_status_switcher["PLANNED"],
        "includes_advisories": includes_advisories_switcher["NO_ADVISORIES"],
    }
