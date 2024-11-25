from dataclasses import dataclass
from api.dto.volumes.nested.circle.circle_center import CircleCenterDto
from api.dto.volumes.nested.circle.circle_radius import CircleRadiusDto


@dataclass
class OutlineCircleDto:
    center: CircleCenterDto
    radius: CircleRadiusDto
