from dataclasses import dataclass
from dto.oir.nested.reference.reference import OirReferenceDto


@dataclass
class GetOirByIdDto:
    operational_intent_reference: OirReferenceDto
