from pydantic import BaseModel
from typing import Optional, List, Dict

# -----------------------------
# Feature Details (simple)
# -----------------------------
class ProjectorDetails(BaseModel):
    type: Optional[str] = None
    resolution: Optional[str] = None


class SoundSystemDetails(BaseModel):
    type: Optional[str] = None
    speakers: Optional[int] = None


class Features(BaseModel):
    projector: Optional[ProjectorDetails] = None
    sound_system: Optional[SoundSystemDetails] = None


# -----------------------------
# Main Theatre Model
# -----------------------------
class Theatre(BaseModel):
    name: str
    description: str
    location: str
    capacity: int

    image: Optional[str] = None
    video: Optional[str] = None

    base_price_per_hr: float
    price_per_person: float

    features: Optional[Features] = None

    projector_detail: Optional[str] = None
    sound_system: Optional[str] = None
    others: Optional[str] = None