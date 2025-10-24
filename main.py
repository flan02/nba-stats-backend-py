# Connect our service with FastAPI
from fastapi import FastAPI
from app.api.routes import (
    boxscore,
    lineups,
    players_avg_total,
    teams,
    players_data,
    games,
)

app = FastAPI(
    title="NBA API Server",
    description="Service FastAPI to retrieve NBA teams and players information",
    version="1.0.0",
)

# Create routes
app.include_router(teams.router, prefix="/teams", tags=["Teams"])
# http://127.0.0.1:8000/players_data/{player_name| All}
app.include_router(players_data.router, prefix="/players_data", tags=["Players"])
# http://127.0.0.1:8000/games/team_id/season/RS|PO
app.include_router(games.router, prefix="/games", tags=["Games"])
# http://127.0.0.1:8000/boxscore/{game_id}/{team_abbr}
app.include_router(boxscore.router, prefix="/boxscore", tags=["Player Stats"])
# http://127.0.0.1:8000/lineups/0022400061/1610612738/bench|starters|all
app.include_router(lineups.router, prefix="/lineups", tags=["Starters vs Bench"])
# http://127.0.0.1:8000/players_stats/RS|PO/{player_id}
app.include_router(
    players_avg_total.router, prefix="/players_stats", tags=["Players Data"]
)


@app.get("/")
def root():
    return {"message": "NBA API Server is running 🚀"}


# TODO: Run our server -> uvicorn main:app --reload

# http://127.0.0.1:8000/docs
