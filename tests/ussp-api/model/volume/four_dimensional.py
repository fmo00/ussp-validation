from model.time.value import TimeValue
from model.volume.three_dimensional import Volume3d

from pydantic import BaseModel


class Volume4d(BaseModel):
    volume: Volume3d
    time_start: TimeValue
    time_end: TimeValue