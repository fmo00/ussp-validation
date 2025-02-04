from pydantic import BaseModel
from model.time.time_value import TimeValue


class OirReference(BaseModel):
    id: str
    flight_type: str
    manager: str
    uss_availability: str
    version: int
    state: str
    ovn: str
    time_start: TimeValue
    time_end: TimeValue
    uss_base_url: str
    subscription_id: str
