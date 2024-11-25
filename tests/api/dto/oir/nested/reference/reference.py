from api.dto.oir.nested.time import TimeValueDto
from dataclasses import dataclass


@dataclass
class OirReferenceDto:
    id: str
    flight_type: str
    manager: str
    uss_availability: str
    version: int
    state: str
    ovn: str
    time_start: TimeValueDto
    time_end: TimeValueDto
    uss_base_url: str
    subscription_id: str
