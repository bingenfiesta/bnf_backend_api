import os
from dotenv import load_dotenv
import urllib.parse

load_dotenv()

import motor.motor_asyncio
from beanie import init_beanie

# Import all your Beanie models here
from src.models.theatre_model import Theatre
# 👆 Add more models as you create them


async def init_db():
    """
    Initialize MongoDB connection and register all Beanie models dynamically.
    Each model's `Settings.name` determines its collection name.
    """
    # Select database
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    password = urllib.parse.quote_plus(password)  # escape special chars
    conn_str = f"mongodb+srv://{username}:{password}@bnfcluster.aqgtwve.mongodb.net/?retryWrites=true&w=majority"
    # Create Motor client (async MongoDB driver)
    client = motor.motor_asyncio.AsyncIOMotorClient(conn_str)
    db = client["BNF"]

    # Register all models with Beanie
    await init_beanie(
        database=db,
        document_models=[
            Theatre
            # Add more models here
        ]
    )
