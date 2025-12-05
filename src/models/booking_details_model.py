from pydantic import BaseModel


class Booking(BaseModel):
    ID: str
    name_of_person: str
    contact: int
    total_price: float
    theatre_id: str
    slot_id: str
    number_of_people: int
    addons: list[str]
    addon_options: list[str]
    decoration_id: str
    note: str
    advance_payment: float
    coupon_id: str
    booking_status: str
    booking_date: int  # Epoch time
    email: str
    discount_price: float
    billing_status: str
    communication_status: str
    txn_ids: list[str]


class BookingList(BaseModel):
    bookings: list[Booking]
