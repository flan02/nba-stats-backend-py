# Endpoint to get player stats
from fastapi import APIRouter
from nba_api.stats.static import players

router = APIRouter()


@router.get("/")
def get_all_players():
    nba_players = players.get_players()

    # Filter only active players
    active_players = [p for p in nba_players if p["is_active"]]

    return {"count": len(active_players), "players": active_players}
