from fastapi import APIRouter
from nba_api.stats.endpoints import leaguegamefinder


router = APIRouter()


# Get access to team game logs
@router.get("/")
def get_team_games():
    games = leaguegamefinder.LeagueGameFinder(
        team_id_nullable="1610612738",  # "1610612745"
        season_nullable="2024-25",
        season_type_nullable="Regular Season",
    )

    df_games = games.get_data_frames()[0]
    print(df_games.head())
    return df_games.to_dict(orient="records")
