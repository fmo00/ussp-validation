from model.time.time_value import TimeValue
from model.volume.volume_3d import Volume3d

from pydantic import BaseModel


class Volume4d(BaseModel):
    volume: Volume3d
    time_start: TimeValue
    time_end: TimeValue
