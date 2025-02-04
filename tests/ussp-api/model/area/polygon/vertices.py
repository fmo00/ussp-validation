from pydantic import BaseModel


class PolygonVertices(BaseModel):
    lng: int
    lat: int
