from pydantic import BaseModel, Field, field_validator
from pydantic.config import ConfigDict


class ProjectorDetails(BaseModel):
    ID: str


class SoundSystemDetails(BaseModel):
    ID: str


class Features(BaseModel):
    projector: ProjectorDetails | None = None
    sound_system: SoundSystemDetails | None = None


class Theatre(BaseModel):
    # Python-friendly attribute names with DB aliases
    id: str = Field(..., alias="_id")
    name: str = Field(..., alias="Name")
    location: str = Field(..., alias="Location")
    price_per_person: float = Field(..., alias="PricePerPerson")
    description: str = Field(..., alias="Description")
    capacity: int = Field(..., alias="Capacity")
    price_per_hour: float = Field(0.0, alias="PricePerHour")
    images: list[str] = Field(default_factory=list, alias="Images")
    video: str = Field(..., alias="Video")
    features: Features | None = None
    delete: bool = False

    model_config = ConfigDict(populate_by_name=True)

    @field_validator("capacity", mode="before")
    @classmethod
    def _parse_capacity(cls, v):
        if v is None:
            return 0
        if isinstance(v, int):
            return v
        if isinstance(v, str):
            v = v.strip()
            if v.isdigit():
                return int(v)
            try:
                return int(float(v))
            except Exception:
                raise ValueError("capacity must be an int or numeric string")
        raise ValueError("capacity must be an int or numeric string")

    @field_validator("price_per_hour", mode="before")
    @classmethod
    def _parse_price_per_hour(cls, v):
        if v is None:
            return 0.0
        if isinstance(v, (int, float)):
            return float(v)
        if isinstance(v, str):
            v = v.strip()
            try:
                return float(v)
            except Exception:
                raise ValueError("price_per_hour must be a number or numeric string")
        raise ValueError("price_per_hour must be a number or numeric string")

    @field_validator("images", mode="before")
    @classmethod
    def _parse_images(cls, v):
        # Accept semicolon-separated string or list
        if v is None:
            return []
        if isinstance(v, list):
            return [str(x).strip() for x in v if x is not None]
        if isinstance(v, str):
            # split on semicolon or comma
            parts = [p.strip() for p in v.split(";") if p.strip()]
            if not parts:
                parts = [p.strip() for p in v.split(",") if p.strip()]
            return parts
        return [str(v)]


class TheatresList(BaseModel):
    theaters: list[Theatre]


if __name__ == "__main__":
    sample = {
        "_id": "692130eecd96499afbc54d3b",
        "Name": "Royal Theater",
        "Location": "Gachibowli, Hyderabad",
        "PricePerPerson": 399.0,
        "Description": "Premium royal-themed private theater with luxury seating.",
        "Capacity": "18",
        "PricePerHour": "1600",
        "Images": "royal1.jpg;royal2.jpg",
        "Video": "royal.mp4",
    }
    t = Theatre.model_validate(sample)
    print(t.model_dump())
