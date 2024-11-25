from dataclasses import dataclass
from api.dto.oir.nested.time.time import TimeValueDto
from api.dto.volumes.nested.volume_3d import Volume3dDto


@dataclass
class Volume4dDto:
    volume: Volume3dDto
    time_start: TimeValueDto
    time_end: TimeValueDto
