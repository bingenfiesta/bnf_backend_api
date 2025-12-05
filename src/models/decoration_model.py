from pydantic import BaseModel


class Decoration(BaseModel):
    ID: str
    name: str
    price: float
    theatre_id: str
    slot_id: str
    image: str
    video: str
    description: str


class DecorationsList(BaseModel):
    decorations: list[Decoration]
