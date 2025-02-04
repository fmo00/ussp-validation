from typing import Optional
from pydantic import BaseModel

from model.time.time_value import TimeValue


class ConstraintReference(BaseModel):
    id: str
    manager: str
    uss_availability: str
    version: int
    ovn: Optional[str] = None
    time_start: TimeValue
    time_end: TimeValue
    uss_base_url: str
