from fastapi import APIRouter, HTTPException
from src.models.theatre_model import Theatre
from src.core.db_operations.theatre_operations import get_complete_theatre_list,add_new_theatre, delete_theatre

router = APIRouter(prefix="/theatre", tags=["Theatre Operations"])

@router.get("/list")
def get_list(start=0, page_size=10, page_num=1):
    return get_complete_theatre_list(start=0, page_size=10, page_num=1)

@router.post("/new")
def add_new(theatre:Theatre):
    result = add_new_theatre(theatre)
    return result

@router.patch("/{id}")
def update_one(id:str):
    return {}

@router.delete("/{id}")
def delete_one(id:str):
    try:
        result = delete_theatre(id)
        if not result:
            HTTPException(status_code=422, detail="Failed to Delete" )
    except Exception as e:
        HTTPException(status_code=500, detail=f"Failed to Delete : {str(e)}" )

    return {"status": "success"}

