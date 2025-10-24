# Endpoint to get player stats
from fastapi import APIRouter
from nba_api.stats.static import players

router = APIRouter()


@router.get(
    "/"
)  # TODO: build up this api to receive via url -> send player name and get his id
def get_all_players():
    nba_players = players.get_players()

    # Filter only active players
    active_players = [p for p in nba_players if p["is_active"]]
    # celtics_players = [
    #     p for p in active_players if p["full_name"] == "Jaylen Brown"
    # ]  # Celtics team ID

    # return {"count": len(active_players), "celtics_players": celtics_players}
    return {"count": len(active_players), "players": active_players}
