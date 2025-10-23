# Endpoint to get team stats
from typing import List
from fastapi import APIRouter, Query, HTTPException
from nba_api.stats.static import teams
from nba_api.stats.endpoints import commonteamroster

from app.api.models.models import RosterResponse, Teams

router = APIRouter()


# Static endpoint to get all teams
@router.get("/", response_model=List[Teams])
def get_all_teams(team_name: str = Query(None, description="Filter teams by name")):
    nba_teams = teams.get_teams()
    # filtering by team name if provided
    if team_name:
        nba_teams = [
            team for team in nba_teams if team_name.lower() in team["full_name"].lower()
        ]
    return [Teams(**team) for team in nba_teams]


# Dynamic endpoint to get team roster by team ID -> (celtics id: 1610612738)
@router.get("/{team_id}/players", response_model=RosterResponse)
def get_team_players(team_id: int):
    try:
        roster = commonteamroster.CommonTeamRoster(team_id=team_id)
        df = roster.get_data_frames()[0]
        players_list = df.to_dict(orient="records")
        # print({"team_id": team_id, "count": len(players_list), "players": players_list})
        return RosterResponse(
            team_id=team_id, count=len(players_list), players=players_list
        )
    except Exception as e:
        raise HTTPException(
            status_code=404, detail=f"Team not found on error: {str(e)}"
        )
