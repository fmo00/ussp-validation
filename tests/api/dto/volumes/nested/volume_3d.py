from api.dto.volumes.nested.altitude import AltitudeDto
from api.dto.volumes.nested.circle.outline_circle import OutlineCircleDto
from api.dto.volumes.nested.polygon.outline_polygon import OutlinePolygonDto
from pydantic import BaseModel


class Volume3dDto(BaseModel):
    outline_circle: OutlineCircleDto
    outline_polygon: OutlinePolygonDto
    altitude_lower: AltitudeDto
    altitude_upper: AltitudeDto
