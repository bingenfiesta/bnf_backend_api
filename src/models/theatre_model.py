from beanie import Document
from pydantic import BaseModel
from typing import Optional, List

class ProjectorDetails(BaseModel):
    brand: Optional[str] = None
    resolution: Optional[str] = None
    lumens: Optional[int] = None


class SoundSystemDetails(BaseModel):
    brand: Optional[str] = None
    channels: Optional[int] = None
    power_watts: Optional[int] = None


class Features(BaseModel):
    projector: Optional[ProjectorDetails] = None
    sound_system: Optional[SoundSystemDetails] = None


class Theatre(Document):
    ID: str
    name: str
    description: Optional[str] = None
    location: str
    capacity: int
    images: List[str] = []
    video: Optional[str] = None
    base_price_per_hr: float
    price_per_person: float
    features: Optional[Features] = None

    class Settings:
        name = "theatres"
