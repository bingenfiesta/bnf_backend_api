from pydantic import BaseModel


class ProjectorDetails(BaseModel):
    ID: str


class SoundSystemDetails(BaseModel):
    ID: str


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


class TheatresList(BaseModel):
    theaters: list[Theatre]


if __name__ == "__main__":
    a = SoundSystemDetails(ID="1A")
    print(a.model_validate())
