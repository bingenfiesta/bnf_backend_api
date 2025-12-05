from pydantic import BaseModel


class Addon(BaseModel):
    ID: str
    name: str
    description: str
    location: str
    capacity: int
    image: str
    video: str
    category: str
    price: float
    # options: list[Options] # TODO: add options


class AddonsList(BaseModel):
    addons: list[Addon]
