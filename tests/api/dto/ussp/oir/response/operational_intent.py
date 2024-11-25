from dataclasses import dataclass
from api.dto.oir.nested.reference.reference import OirReferenceDto


@dataclass
class OperationalIntentDto:
    reference: OirReferenceDto
