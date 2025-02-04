from pydantic import BaseModel

from model.volume.volume_4d import Volume4d


class FlightBasicInformation(BaseModel):
    usage_state: str
    uas_state: str
    area: Volume4d
