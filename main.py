from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.utils.constants import Collections
from src.utils.db_operations.db_operations import BnFMongoManager

# from routes import (
#     theatre_routes,
#     slots_routes
# )


@asynccontextmanager
async def lifespan(app: FastAPI):

    # Initializing the DB Objects that can be reused
    for collection_name in Collections:
        collection_name.value.connection = BnFMongoManager(
            collection_name.value.collection_name
        )
    yield


app = FastAPI(title="Binge N Fiesta API service", version="0.1", lifespan=lifespan)


# Register routers
# app.include_router(theatre_routes.router)
# app.include_router(slots_routes.router)


@app.get("/")
def root():
    return {"message": "Welcome to BNF"}
