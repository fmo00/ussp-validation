from pydantic import BaseModel


class Altitude(BaseModel):
    value: int
    reference: str
    units: str