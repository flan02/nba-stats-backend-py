from fastapi import APIRouter
from nba_api.stats.endpoints import leaguegamefinder


router = APIRouter()


# Get access to team game logs
@router.get("/{team_id}/{season}/{type}")  # season: 2024-25type: RS | PO
def get_team_games(team_id: str, season: str, type: str):
    if type == "RS":
        type = "Regular Season"
    elif type == "PO":
        type = "Playoffs"
    games = leaguegamefinder.LeagueGameFinder(
        team_id_nullable=team_id,  # - 1610612738
        season_nullable=season,
        season_type_nullable=type,
    )

    df_games = games.get_data_frames()[0]
    print(df_games.head())
    return df_games.to_dict(orient="records")
