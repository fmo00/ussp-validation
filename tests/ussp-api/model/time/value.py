from pydantic import BaseModel


class TimeValue(BaseModel):
    value: str
    format: str