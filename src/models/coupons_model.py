from enum import Enum

from pydantic import BaseModel


class TypeOfCoupon(Enum):
    percentage = "Percentage"
    flat = "Flat"


class Coupon(BaseModel):
    ID: str
    name: str
    start: int  # Epoch time
    end: int  # Epoch time
    count: int
    coupon_code: str
    theatre_id: str
    type_of_coupon: TypeOfCoupon  # Flat / Percentage
    value: float
    description: str
    # conditions: list[Conditions]


class CouponsList(BaseModel):
    coupons: list[Coupon]
