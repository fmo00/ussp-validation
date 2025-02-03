from pydantic import BaseModel


class CircleCenter(BaseModel):
    value: int
    units: str
