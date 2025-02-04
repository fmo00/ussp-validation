from pydantic import BaseModel
from model.area.circle.center import CircleCenter
from model.area.circle.radius import CircleRadius


class CircleOutline(BaseModel):
    center: CircleCenter
    radius: CircleRadius
