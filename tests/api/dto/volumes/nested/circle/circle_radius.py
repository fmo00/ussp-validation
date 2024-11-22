from dataclasses import dataclass


@dataclass
class CircleRadiusDto:
    value: int
    units: str
