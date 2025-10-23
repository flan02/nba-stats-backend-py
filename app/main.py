# Connect our service with FastAPI
from fastapi import FastAPI
from app.api.routes import teams, players

app = FastAPI(
    title="NBA API Server",
    description="Service FastAPI to retrieve NBA teams and players information",
    version="1.0.0",
)

# Create routes
app.include_router(teams.router, prefix="/teams", tags=["Teams"])
app.include_router(players.router, prefix="/players", tags=["Players"])


@app.get("/")
def root():
    return {"message": "NBA API Server is running 🚀"}


# TODO: Run our server -> uvicorn app.main:app --reload

# http://127.0.0.1:8000/docs
