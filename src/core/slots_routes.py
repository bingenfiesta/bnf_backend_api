import csv
from datetime import datetime
from io import StringIO

from config.db_config import MongoDBHandler
from fastapi import APIRouter, File, HTTPException, UploadFile

router = APIRouter(prefix="/api/slots", tags=["Slots"])

# Initialize DB handler
db_handler = MongoDBHandler(db_name="BNF", collection_name="Slot")
db_handler.connect()

@router.post("/upload_csv")
async def upload_slot_csv(file: UploadFile = File(...)):
    """
    Ingest theatres data from a CSV file into MongoDB.
    Expected CSV headers: ID, Name, Location, PricePerPerson
    """
    try:
        content = await file.read()
        decoded = content.decode("utf-8")
        reader = csv.DictReader(StringIO(decoded))

        slots = []
        for row in reader:
            slot = {
                "Name": row["Name"],
                "End": datetime.strptime(row["End"],"%d-%m-%Y %H:%M"),
                "Start": datetime.strptime(row["Start (Date & Time)"], "%d-%m-%Y %H:%M"),
                "Coupon" : row["Applied coupon (YES/NO)"],
                "Theatre" : row["Theatre ID"],
                "Price" : row["price"]
            }
            slots.append(slot)

        if slots:
            inserted_ids = db_handler.insert_many(slots)
            return {"message": f"Inserted {len(inserted_ids)} slots successfully"}
        else:
            raise HTTPException(status_code=400, detail="CSV file is empty or invalid")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")
