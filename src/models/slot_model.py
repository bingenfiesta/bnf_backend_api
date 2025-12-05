from pydantic import BaseModel


class Slot(BaseModel):
    ID: str
    name: str
    start: int  # Epoch time
    end: int  # Epoch time
    price: float
    theatre_id: str
    applied_coupon: str


class SlotsList(BaseModel):
    slots: list[Slot]
