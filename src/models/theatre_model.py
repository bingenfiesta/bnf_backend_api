from pydantic import BaseModel


class ProjectorDetails(BaseModel):
    pass


class SoundSystemDetails(BaseModel):
    pass


class Features(BaseModel):
    # Note: Other classes need to be added for new features
    projector: ProjectorDetails
    sound_system: SoundSystemDetails


class Theatre(BaseModel):
    ID: str
    name: str
    description: str
    location: str
    capacity: int
    image: str
    video: str
    base_price_per_hr: float
    price_per_person: float
    features: Features
