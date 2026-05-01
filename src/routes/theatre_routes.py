# src/routes/theatre_routes.py

from fastapi import APIRouter, HTTPException
from bson import ObjectId
from src.utils.db_operations.db_operations import theatres_collection
from src.models.theathre_model import Theatre

router = APIRouter()

# Get all theatres
@router.get("/theatres")
def get_all_theatres():
    theatres = []
    for theatre in theatres_collection.find():
        theatre["_id"] = str(theatre["_id"])
        theatres.append(theatre)
    return theatres


# Get one theatre
@router.get("/theatres/{theatre_id}")
def get_one_theatre(theatre_id: str):

    # 1. Validate ObjectId format
    if not ObjectId.is_valid(theatre_id):
        raise HTTPException(status_code=400, detail="Invalid theatre ID format")

    # 2. Fetch from DB
    theatre = theatres_collection.find_one({"_id": ObjectId(theatre_id)})

    # 3. If not found
    if theatre is None:
        raise HTTPException(status_code=404, detail="Theatre not found")

    # 4. Convert ObjectId to string
    theatre["_id"] = str(theatre["_id"])

    return theatre

# Create theatre
@router.post("/theatres")
def create_theatre(new_theatre: Theatre):

    # Convert model → dict
    theatre_dict = new_theatre.dict()

    result = theatres_collection.insert_one(theatre_dict)

    return {
        "message": "Theatre created!",
        "id": str(result.inserted_id)
    }


# Update theatre
@router.put("/theatres/{theatre_id}")
def update_theatre(theatre_id: str, updated_data: dict):

    # 1. Validate ObjectId format
    if not ObjectId.is_valid(theatre_id):
        raise HTTPException(status_code=400, detail="Invalid theatre ID format")

    # 2. Check if theatre exists
    existing = theatres_collection.find_one({"_id": ObjectId(theatre_id)})
    if not existing:
        raise HTTPException(status_code=404, detail="Theatre not found")

    # Prevent updating _id
    if "_id" in updated_data:
        raise HTTPException(status_code=400, detail="Cannot update _id")
    
    # 3. Prevent empty update
    if not updated_data:
        raise HTTPException(status_code=400, detail="No data provided to update")       

    # 4. Business validations (optional but recommended)
    if "capacity" in updated_data and updated_data["capacity"] <= 0:
        raise HTTPException(status_code=400, detail="Capacity must be greater than 0")

    if "base_price_per_hr" in updated_data and updated_data["base_price_per_hr"] < 0:
        raise HTTPException(status_code=400, detail="Base price must be >= 0")

    # 5. Perform update
    result = theatres_collection.update_one(
        {"_id": ObjectId(theatre_id)},
        {"$set": updated_data}
    )

    # 6. Check if anything actually changed
    if result.modified_count == 0:
        return {"message": "No changes made (data same as existing)"}

    return {"message": "Theatre updated successfully"}

# Delete theatre
@router.delete("/theatres/{theatre_id}")
def delete_theatre(theatre_id: str):

    if not ObjectId.is_valid(theatre_id):
        raise HTTPException(status_code=400, detail="Invalid theatre ID format")

    result = theatres_collection.delete_one({"_id": ObjectId(theatre_id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Theatre not found")

    return {"message": "Theatre deleted successfully"}
    