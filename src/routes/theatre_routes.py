from fastapi import APIRouter, HTTPException, Body
from src.models.theatre_model import Theatre
from src.core.db_operations.theatre_operations import get_complete_theatre_list,add_new_theatre, delete_theatre, update_theatre

router = APIRouter(prefix="/theatre", tags=["Theatre Operations"])

@router.get("/list")
def get_list(start: int = 0, page_size: int = 10, page_num: int = 1):
    return get_complete_theatre_list(start=start, page_size=page_size, page_num=page_num)

@router.post("/new")
def add_new(theatre:Theatre):
    result = add_new_theatre(theatre)
    return result

@router.patch("/{id}")
def update_one(id: str, updates: dict = Body(...)):
    try:
        modified = update_theatre(id, updates)
        if modified == 0:
            raise HTTPException(status_code=422, detail="No document updated")
        return {"status": "success"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{id}")
def delete_one(id:str):
    try:
        result = delete_theatre(id)
        if not result:
            raise HTTPException(status_code=422, detail="Failed to Delete" )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to Delete : {str(e)}" )

    return {"status": "success"}

