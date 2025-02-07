from pydantic import BaseModel


class CircleRadius(BaseModel):
    value: int
    units: str