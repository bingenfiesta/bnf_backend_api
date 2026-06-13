from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.utils.constants import Collections
from src.utils.db_helper.db_helper import BnFMongoManager

from src.routes import theatre_routes
from src.routes import slots_routes, bookings_routes

@asynccontextmanager
async def lifespan(app: FastAPI):

    # Initializing the DB Objects that can be reused
    for collection_name in Collections:
        collection_name.value.connection = BnFMongoManager(collection_name.value.collection_name)
    yield


app = FastAPI(title="Binge N Fiesta API service", version="0.1", lifespan=lifespan)


# Register routers
app.include_router(theatre_routes.router)
app.include_router(slots_routes.router)
app.include_router(bookings_routes.router)


@app.get("/")
def root():
    return {"message": "Welcome to BNF"}
