from fastapi import FastAPI

from src.routes.theatre_routes import router as theatre_router
from src.routes.slot_routes import router as slot_router

app = FastAPI()

# include routers
app.include_router(theatre_router)
app.include_router(slot_router)


@app.get("/")
def home():
    return {"message": "BNF Backend is running!"}


#from fastapi import FastAPI,HTTPException
#from src.utils.db_operations.db_operations import theatres_collection, slots_collection
#from src.models.theathre_model import Theatre
#from bson import ObjectId
#from datetime import datetime
#
#app = FastAPI()
#
#@app.get("/")
#def home():
#    return {"message": "BNF Backend is running!"}
#
## Get all theatres
#@app.get("/theatres")
#def get_all_theatres():
#    theatres = []
#    for theatre in theatres_collection.find():
#        theatre["_id"] = str(theatre["_id"])
#        theatres.append(theatre)
#    return theatres
#
## Get one theatre
#@app.get("/theatres/{theatre_id}")
#def get_one_theatre(theatre_id: str):
#
#    # 1. Validate ObjectId format
#    if not ObjectId.is_valid(theatre_id):
#        raise HTTPException(status_code=400, detail="Invalid theatre ID format")
#
#    # 2. Fetch from DB
#    theatre = theatres_collection.find_one({"_id": ObjectId(theatre_id)})
#
#    # 3. If not found
#    if theatre is None:
#        raise HTTPException(status_code=404, detail="Theatre not found")
#
#    # 4. Convert ObjectId to string
#    theatre["_id"] = str(theatre["_id"])
#
#    return theatre
#
## Create a theatre
#@app.post("/theatres")
#def create_theatre(new_theatre: Theatre):
#
#    # Convert model → dict
#    theatre_dict = new_theatre.dict()
#
#    result = theatres_collection.insert_one(theatre_dict)
#
#    return {
#        "message": "Theatre created!",
#        "id": str(result.inserted_id)
#    }
#
## Update a theatre
#@app.put("/theatres/{theatre_id}")
#def update_theatre(theatre_id: str, updated_data: dict):
#
#    # 1. Validate ObjectId format
#    if not ObjectId.is_valid(theatre_id):
#        raise HTTPException(status_code=400, detail="Invalid theatre ID format")
#
#    # 2. Check if theatre exists
#    existing = theatres_collection.find_one({"_id": ObjectId(theatre_id)})
#    if not existing:
#        raise HTTPException(status_code=404, detail="Theatre not found")
#
#    # Prevent updating _id
#    if "_id" in updated_data:
#        raise HTTPException(status_code=400, detail="Cannot update _id")
#    
#    # 3. Prevent empty update
#    if not updated_data:
#        raise HTTPException(status_code=400, detail="No data provided to update")       
#
#    # 4. Business validations (optional but recommended)
#    if "capacity" in updated_data and updated_data["capacity"] <= 0:
#        raise HTTPException(status_code=400, detail="Capacity must be greater than 0")
#
#    if "base_price_per_hr" in updated_data and updated_data["base_price_per_hr"] < 0:
#        raise HTTPException(status_code=400, detail="Base price must be >= 0")
#
#    # 5. Perform update
#    result = theatres_collection.update_one(
#        {"_id": ObjectId(theatre_id)},
#        {"$set": updated_data}
#    )
#
#    # 6. Check if anything actually changed
#    if result.modified_count == 0:
#        return {"message": "No changes made (data same as existing)"}
#
#    return {"message": "Theatre updated successfully"}
#
## Delete a theatre
#@app.delete("/theatres/{theatre_id}")
#def delete_theatre(theatre_id: str):
#
#    if not ObjectId.is_valid(theatre_id):
#        raise HTTPException(status_code=400, detail="Invalid theatre ID format")
#
#    result = theatres_collection.delete_one({"_id": ObjectId(theatre_id)})
#
#    if result.deleted_count == 0:
#        raise HTTPException(status_code=404, detail="Theatre not found")
#
#    return {"message": "Theatre deleted successfully"}
#    
#    
## =========================
## SLOT APIs (CRUD)
## =========================
#
## Create Slot
#@app.post("/slots")
#def create_slot(slot: dict):
#
#    # -----------------------------
#    # 1. Required fields check
#    # -----------------------------
#    required_fields = ["name", "start_time", "end_time", "price", "theatre_id"]
#
#    for field in required_fields:
#        if field not in slot:
#            raise HTTPException(
#                status_code=400,
#                detail=f"Missing required field: {field}"
#            )
#
#    # -----------------------------
#    # 2. Validate theatre_id
#    # -----------------------------
#    if not ObjectId.is_valid(slot["theatre_id"]):
#        raise HTTPException(status_code=400, detail="Invalid theatre_id format")
#
#    theatre = theatres_collection.find_one({"_id": ObjectId(slot["theatre_id"])})
#    if not theatre:
#        raise HTTPException(status_code=404, detail="Theatre not found")
#
#    # -----------------------------
#    # 3. Validate time format & logic
#    # -----------------------------
#    try:
#        start = datetime.strptime(slot["start_time"], "%Y-%m-%d %H:%M")
#        end = datetime.strptime(slot["end_time"], "%Y-%m-%d %H:%M")
#    except:
#        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD HH:MM")
#
#    if start >= end:
#        raise HTTPException(status_code=400, detail="start_time must be before end_time")
#
#    # -----------------------------
#    # 4. Validate price
#    # -----------------------------
#    if slot["price"] < 0:
#        raise HTTPException(status_code=400, detail="Price must be >= 0")
#
#    # -----------------------------
#    # 5. Optional: Prevent overlapping slots
#    # -----------------------------
#    overlapping = slots_collection.find_one({
#    "theatre_id": slot["theatre_id"],
#    "start_time": {"$lt": slot["end_time"]},
#    "end_time": {"$gt": slot["start_time"]}
#    })
#
#    if overlapping:
#        raise HTTPException(status_code=400, detail="Slot overlaps with existing slot")
#
#    # -----------------------------
#    # 6. Insert into DB
#    # -----------------------------
#    result = slots_collection.insert_one(slot)
#
#    return {
#        "message": "Slot created!",
#        "id": str(result.inserted_id)
#    }
#
#
## Get All Slots
#@app.get("/slots")
#def get_all_slots():
#    slots = []
#    for slot in slots_collection.find():
#        slot["_id"] = str(slot["_id"])
#        slots.append(slot)
#    return slots
#
#
## Get One Slot
#@app.get("/slots/{slot_id}")
#def get_one_slot(slot_id: str):
#
#    # 1. Validate ObjectId format
#    if not ObjectId.is_valid(slot_id):
#        raise HTTPException(status_code=400, detail="Invalid slot ID format")
#
#    # 2. Fetch from DB
#    slot = slots_collection.find_one({"_id": ObjectId(slot_id)})
#
#    # 3. If not found
#    if slot is None:
#        raise HTTPException(status_code=404, detail="Slot not found")
#
#    # 4. Convert ObjectId to string
#    slot["_id"] = str(slot["_id"])
#
#    return slot
#
## Update Slot
#@app.put("/slots/{slot_id}")
#def update_slot(slot_id: str, updated_data: dict):
#
#    # 1. Validate ObjectId format
#    if not ObjectId.is_valid(slot_id):
#        raise HTTPException(status_code=400, detail="Invalid slot ID format")
#
#    # 2. Check if slot exists
#    existing = slots_collection.find_one({"_id": ObjectId(slot_id)})
#    if not existing:
#        raise HTTPException(status_code=404, detail="Slot not found")
#
#    # 3. Prevent empty update
#    if not updated_data:
#        raise HTTPException(status_code=400, detail="No data provided to update")
#
#    # 4. Business validations
#
#    # Price validation
#    if "price" in updated_data and updated_data["price"] < 0:
#        raise HTTPException(status_code=400, detail="Price must be >= 0")
#
#    # Time validation (if provided)
#    if "start_time" in updated_data or "end_time" in updated_data:
#        try:
#            start = updated_data.get("start_time", existing["start_time"])
#            end = updated_data.get("end_time", existing["end_time"])
#
#            start_dt = datetime.strptime(start, "%Y-%m-%d %H:%M")
#            end_dt = datetime.strptime(end, "%Y-%m-%d %H:%M")
#
#            if start_dt >= end_dt:
#                raise HTTPException(status_code=400, detail="start_time must be before end_time")
#
#        except ValueError:
#            raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD HH:MM")
#
#    # Prevent updating _id
#    if "_id" in updated_data:
#        raise HTTPException(status_code=400, detail="Cannot update _id")
#
#    # 5. Perform update
#    result = slots_collection.update_one(
#        {"_id": ObjectId(slot_id)},
#        {"$set": updated_data}
#    )
#
#    # 6. Check if anything actually changed
#    if result.modified_count == 0:
#        return {"message": "No changes made (data same as existing)"}
#
#    return {"message": "Slot updated successfully"}
#
## Delete Slot
#@app.delete("/slots/{slot_id}")
#def delete_slot(slot_id: str):
#
#    # 1. Validate ObjectId format
#    if not ObjectId.is_valid(slot_id):
#        raise HTTPException(status_code=400, detail="Invalid slot ID format")
#
#    # 2. Perform delete
#    result = slots_collection.delete_one({"_id": ObjectId(slot_id)})
#
#    # 3. Check if slot existed
#    if result.deleted_count == 0:
#        raise HTTPException(status_code=404, detail="Slot not found")
#
#    return {"message": "Slot deleted successfully"}