from fastapi import APIRouter, HTTPException
from src.models.booking_details_model import Booking
from src.core.db_operations.booking_operations import get_bookings_list, add_new_booking, delete_booking
from fastapi import Body
from src.core.db_operations.booking_operations import update_booking

router = APIRouter(prefix="/bookings", tags=["Bookings Operations"])


@router.get("/list")
def get_list(start: int = 0, page_size: int = 10, page_num: int = 1):
    return get_bookings_list(start=start, page_size=page_size, page_num=page_num)


@router.post("/new")
def add_new(booking: Booking):
    try:
        result = add_new_booking(booking)
        return {"id": result}
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))


@router.delete("/{id}")
def delete_one(id: str):
    try:
        result = delete_booking(id)
        if not result:
            raise HTTPException(status_code=422, detail="Failed to Delete")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"status": "success"}


@router.patch("/{id}")
def update_one(id: str, updates: dict = Body(...)):
    try:
        modified = update_booking(id, updates)
        if modified == 0:
            raise HTTPException(status_code=422, detail="No document updated")
        return {"status": "success"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
