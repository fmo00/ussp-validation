from model.area.volume_4d import Volume4d

from pydantic import BaseModel
from typing import Optional


class OirDetails(BaseModel):
    volumes: Optional[Volume4d] = None
    off_nominal_volumes: Optional[Volume4d] = None
    priority: Optional[int] = None
