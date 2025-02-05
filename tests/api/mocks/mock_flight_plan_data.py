from . import FlightAuthorisationDataDto, OperationIntentInformationDto
from . import operation_mode_switcher
from . import uas_class_switcher

from faker import Faker
from uuid import uuid4


class FlightPlanMocks:
    fake = Faker()

    ASTM_F3548_21_OP_INTENT: OperationIntentInformationDto = {"priority": 0}

    USPACE_FLIGHT_AUTH_DATA: FlightAuthorisationDataDto = {
        "uas_serial_number": uuid4(),
        "operation_mode": operation_mode_switcher["UNDECLARED"],
        "operation_category": "open",
        "uas_class": uas_class_switcher["C0"],
        "identification_technologies": ["ASTMNetRID"],
        "connectivity_methods": ["phone"],
        "endurance_minutes": fake.random_number(),
        "emergency_procedure_url": fake.url(),
        "operator_id": uuid4(),
    }

    FLIGHT_PLAN_INJECTION_REQUEST = {}
