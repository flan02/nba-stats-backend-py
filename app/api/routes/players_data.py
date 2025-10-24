# Endpoint to get player stats
from fastapi import APIRouter
from nba_api.stats.static import players

router = APIRouter()


# TODO: build up this api to receive via url -> send player name and get his id
@router.get("/{player_name}")
def get_player_by_name(player_name: str):
    nba_players = players.get_players()

    # Filter only active players
    active_players = [p for p in nba_players if p["is_active"]]

    if player_name == "All":
        return {"count": len(active_players), "players": active_players}

    selected_player = [p for p in active_players if p["full_name"] == player_name]
    return {"count": len(active_players), "players": selected_player}
