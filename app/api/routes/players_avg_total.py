from typing import List
from fastapi import APIRouter
from nba_api.stats.endpoints import playergamelog

from app.api.models.models import PlayerStatsResponse
from app.services.utils import calculate_shooting_percentages


router = APIRouter()


@router.get("/{type}/{player_id}", response_model=List[PlayerStatsResponse])  # type: RS | PO
def get_player_avg_totals(type: str, player_id: int):
    if type == "RS":
        season_type = "Regular Season"
    elif type == "PO":
        season_type = "Playoffs"
    log = playergamelog.PlayerGameLog(
        player_id=player_id, season="2024-25", season_type_all_star=season_type
    )
    df = log.get_data_frames()[0]

    # Columnas numéricas de estadísticas relevantes
    stats_columns = df.select_dtypes(include="number").columns.tolist()
    # Excluir columnas de ID o flags si no tienen sentido sumar
    stats_columns = [
        c for c in stats_columns if c not in ["Player_ID", "VIDEO_AVAILABLE"]
    ]

    # - Totals
    totals = df[stats_columns].sum(numeric_only=True)
    # Add colum for type: totals or average
    totals["TYPE"] = "TOTAL"
    totals = calculate_shooting_percentages(totals)

    # - Averages
    # averages = df[["PTS", "REB", "AST", "STL", "BLK"]].mean()
    averages = df[stats_columns].mean(numeric_only=True).round(1)
    averages = calculate_shooting_percentages(averages)
    averages["TYPE"] = "AVERAGE"

    return [PlayerStatsResponse(**totals), PlayerStatsResponse(**averages)]
