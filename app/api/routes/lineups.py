from typing import List
from fastapi import APIRouter
from nba_api.stats.endpoints import boxscoretraditionalv2

from app.api.models.models import LineupStatsResponse

router = APIRouter()


@router.get("/{game_id}/{team_id}/{type}", response_model=List[LineupStatsResponse])
def get_lineups(game_id: str, team_id: int, type: str):
    box = boxscoretraditionalv2.BoxScoreTraditionalV2(game_id=game_id)
    stats = box.get_data_frames()

    print("type:", type)

    players_df = stats[2]
    if type.capitalize() == "Starters":
        players_df = players_df[players_df["STARTERS_BENCH"] == type.capitalize()]

    if type.capitalize() == "Bench":
        players_df = players_df[players_df["STARTERS_BENCH"] == type.capitalize()]

    if type.capitalize() == "All":
        pass  # no filtering

    players_df = players_df[players_df["TEAM_ID"] == team_id]

    print(players_df)

    lineups = players_df.to_dict(orient="records")
    return [LineupStatsResponse(**lin) for lin in lineups]
