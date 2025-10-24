from typing import List
from fastapi import APIRouter, HTTPException
from nba_api.stats.endpoints import boxscoretraditionalv2
import pandas as pd
import numpy as np
from app.api.models.models import PlayerBoxScoreResponse

router = APIRouter()

# - 2024 example game ID: 0022401222
# - 0022500083 -> First game of the 2025-26 season


# Get player stats for a specific game
# response_model=List[PlayerBoxScoreResponse]
@router.get("/{game_id}/{team_abbr}", response_model=List[PlayerBoxScoreResponse])
def get_player_stats(game_id: str, team_abbr: str):
    box = boxscoretraditionalv2.BoxScoreTraditionalV2(game_id=game_id)
    stats = box.get_data_frames()
    # [0] for PLAYERS, [1] for TEAM_STATS (same data that /games), [2] for STARTERS + BENCHERS

    players_df = stats[0]

    players_df = players_df.replace(
        [pd.NA, pd.NaT, np.nan, float("inf"), float("-inf")], None
    )
    # $ filtering by team
    players_df = players_df[players_df["TEAM_ABBREVIATION"] == team_abbr.upper()]

    if players_df.empty:
        raise HTTPException(
            status_code=404,
            detail=f"Boxscore not available yet for team abbreviation '{team_abbr}' in game '{game_id}'",
        )

    # ? Convertir a JSON-friendly dict
    players_boxscore = players_df.to_dict(orient="records")

    return [PlayerBoxScoreResponse(**player) for player in players_boxscore]
