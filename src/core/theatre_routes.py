from fastapi import APIRouter, UploadFile, File, HTTPException
import csv
from io import StringIO
from src.models.theatre_model import Theatre, Features, ProjectorDetails, SoundSystemDetails

router = APIRouter(prefix="/api/theatres", tags=["Theatres"])


def safe_int(value, default=0):
    try:
        return int(value)
    except Exception:
        return default


def safe_float(value, default=0.0):
    try:
        return float(value)
    except Exception:
        return default


@router.post("/upload_csv")
async def upload_theatres_csv(file: UploadFile = File(...)):
    """
    Ingest theatres data from a CSV file into MongoDB using Beanie ODM.
    Expected CSV headers:
    ID, Name, Location, PricePerPerson, Description, Capacity, PricePerHour, Images, Video
    """
    try:
        content = await file.read()
        decoded = content.decode("utf-8-sig")  # handle BOM
        reader = csv.DictReader(StringIO(decoded))

        # Normalize headers (strip BOM/whitespace)
        reader.fieldnames = [name.strip().lstrip("\ufeff") for name in reader.fieldnames]

        theatres = []
        for row in reader:
            try:
                print("Processing row:", row)  # DEBUG

                images = row.get("Images", "")
                image_list = images.split(";") if images else []

                theatre = Theatre(
                    ID=row.get("ID", ""),
                    name=row.get("Name", ""),
                    description=row.get("Description", ""),
                    location=row.get("Location", ""),
                    capacity=safe_int(row.get("Capacity")),
                    images=image_list,
                    video=row.get("Video", ""),
                    base_price_per_hr=safe_float(row.get("PricePerHour")),   # map correctly
                    price_per_person=safe_float(row.get("PricePerPerson")), # map correctly
                    features=Features(
                        projector=ProjectorDetails(),
                        sound_system=SoundSystemDetails()
                    )
                )

                print("Parsed theatre object:", theatre.dict())  # DEBUG
                theatres.append(theatre)

            except Exception as row_error:
                import traceback
                print("Row error traceback:", traceback.format_exc())  # DEBUG
                raise HTTPException(
                    status_code=400,
                    detail=f"Invalid row data in row {row}: {row_error}"
                )

        if theatres:
            await Theatre.insert_many(theatres)
            return {"message": f"Inserted {len(theatres)} theatres successfully"}
        else:
            raise HTTPException(status_code=400, detail="CSV file is empty or invalid")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")
