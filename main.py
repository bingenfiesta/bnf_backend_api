from fastapi import FastAPI
import uvicorn
from routes import (
    theatre_routes,
    slots_routes
)

app = FastAPI(title="Event Booking API", version="1.0")

# Register routers
app.include_router(theatre_routes.router)
app.include_router(slots_routes.router)

@app.get("/")
def root():
    return {"message": "Welcome to BNF"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)