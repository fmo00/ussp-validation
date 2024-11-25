from dataclasses import dataclass
from api.dto.volumes.nested.polygon.vertices import PolygonVerticesDto


@dataclass
class OutlinePolygonDto:
    vertices: PolygonVerticesDto
