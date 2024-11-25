from dataclasses import dataclass
from api.dto.ussp.oir.response.operational_intent import OperationalIntentDto


@dataclass
class GetOirByIdDto:
    operational_intent: OperationalIntentDto
