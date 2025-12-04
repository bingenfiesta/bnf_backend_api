from fastapi import FastAPI
from contextlib import asynccontextmanager

import uvicorn
from src.utils.db_operations.db_operations import init_db
from src.core import theatre_routes, slots_routes

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await init_db()
    yield
    # Shutdown (optional cleanup)
    # e.g. close db connections, release resources

app = FastAPI(lifespan=lifespan)

# Routers
app.include_router(theatre_routes.router)
app.include_router(slots_routes.router)


@app.get("/")
def root():
    return {"message": "Welcome to BNF"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8002, reload=True)