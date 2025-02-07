from pydantic import BaseModel
from typing import List

from model.area.polygon.vertices import PolygonVertices


class PolygonOutline(BaseModel):
    vertices: List[PolygonVertices]