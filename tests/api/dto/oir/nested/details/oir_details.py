from dataclasses import dataclass
from api.dto.volumes.volume_4d import Volume4dDto


@dataclass
class OirDetailsDto:
    volumes: Volume4dDto | None
    off_nominal_volumes: Volume4dDto | None
    priority: int | None
