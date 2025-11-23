from fastapi import APIRouter, UploadFile, File, HTTPException
import csv
from io import StringIO
from utils.db_operations.db_operations import MongoDBHandler
from models.theatre import Theatre, Features, ProjectorDetails, SoundSystemDetails  # import your models

router = APIRouter(prefix="/api/theatres", tags=["Theatres"])

# Initialize DB handler
db_handler = MongoDBHandler(db_name="BNF", collection_name="Theatre")
db_handler.connect()

@router.post("/upload_csv")
async def upload_theatres_csv(db_handler, file: UploadFile = File(...)):
    """
    Ingest theatres data from a CSV file into MongoDB.
    Expected CSV headers: ID, Name, Description, Location, Capacity,
    Images, Video, PricePerHour, PricePerPerson, ProjectorBrand, ProjectorResolution,
    ProjectorLumens, SoundBrand, SoundChannels, SoundPower
    """
    try:
        content = await file.read()
        decoded = content.decode("utf-8")
        reader = csv.DictReader(StringIO(decoded))

        theatres = []
        for row in reader:
            try:
                theatre = Theatre(
                    ID=row.get("ID", ""),
                    name=row.get("Name", ""),
                    description=row.get("Description", ""),
                    location=row.get("Location", ""),
                    capacity=int(row.get("Capacity", 0)),
                    image=row.get("Images", ""),
                    video=row.get("Video", ""),
                    base_price_per_hr=float(row.get("PricePerHour", 0)),
                    price_per_person=float(row.get("PricePerPerson", 0)),
                    features=Features(
                        projector=ProjectorDetails(
                            brand=row.get("ProjectorBrand", ""),
                            resolution=row.get("ProjectorResolution", ""),
                            lumens=int(row.get("ProjectorLumens", 0))
                        ),
                        sound_system=SoundSystemDetails(
                            brand=row.get("SoundBrand", ""),
                            channels=int(row.get("SoundChannels", 0)),
                            power_watts=int(row.get("SoundPower", 0))
                        )
                    )
                )
                theatres.append(theatre.dict())  # convert to dict for MongoDB
            except Exception as row_error:
                raise HTTPException(status_code=400, detail=f"Invalid row data: {row_error}")

        if theatres:
            inserted_ids = db_handler.insert_many(theatres)
            return {"message": f"Inserted {len(inserted_ids)} theatres successfully"}
        else:
            raise HTTPException(status_code=400, detail="CSV file is empty or invalid")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")
