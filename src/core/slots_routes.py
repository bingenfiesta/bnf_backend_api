from fastapi import APIRouter, UploadFile, File, HTTPException
import csv
from io import StringIO
from datetime import datetime
from src.models.slot_model import Slot

router = APIRouter(prefix="/api/slots", tags=["Slots"])


@router.post("/upload_csv")
async def upload_slot_csv(file: UploadFile = File(...)):
    """
    Ingest slot data from a CSV file into MongoDB using Beanie ODM.
    Expected CSV headers:
    Name, Start (Date & Time), End, price, Theatre ID, Applied coupon (YES/NO)
    """
    try:
        content = await file.read()
        decoded = content.decode("utf-8")
        reader = csv.DictReader(StringIO(decoded))

        slots = []
        for row in reader:
            try:
                slot = Slot(
                    name=row.get("Name", ""),
                    start=datetime.strptime(row.get("Start (Date & Time)", ""), "%d-%m-%Y %H:%M"),
                    end=datetime.strptime(row.get("End", ""), "%d-%m-%Y %H:%M"),
                    price=float(row.get("price", 0)),
                    theatre_id=row.get("Theatre ID", ""),
                    coupon=row.get("Applied coupon (YES/NO)", ""),
                )
                slots.append(slot)
            except Exception as row_error:
                raise HTTPException(status_code=400, detail=f"Invalid row data: {row_error}")

        if slots:
            await Slot.insert_many(slots)
            return {"message": f"Inserted {len(slots)} slots successfully"}
        else:
            raise HTTPException(status_code=400, detail="CSV file is empty or invalid")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")
