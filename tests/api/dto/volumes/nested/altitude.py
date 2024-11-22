from dataclasses import dataclass


@dataclass
class AltitudeDto:
    value: int
    reference: str
    units: str
