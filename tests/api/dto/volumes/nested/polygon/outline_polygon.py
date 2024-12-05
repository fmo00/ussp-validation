from pydantic import BaseModel
from api.dto.volumes.nested.polygon.vertices import PolygonVerticesDto


class OutlinePolygonDto(BaseModel):
    vertices: PolygonVerticesDto
