from model.area.altitude import Altitude
from model.area.circle.outline import CircleOutline
from model.area.polygon.outline import PolygonOutline

from pydantic import BaseModel
from typing import Optional


class Volume3d(BaseModel):
    outline_circle: Optional[CircleOutline] = None
    outline_polygon: Optional[PolygonOutline] = None
    altitude_lower: Altitude
    altitude_upper: Altitude