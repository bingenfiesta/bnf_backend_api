from beanie import Document
from typing import Optional
from datetime import datetime


class Slot(Document):
    name: str
    start: datetime
    end: datetime
    price: float
    theatre_id: str
    coupon: Optional[str] = None   # "YES"/"NO"

    class Settings:
        name = "slots"  # MongoDB collection name
