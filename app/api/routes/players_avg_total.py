from fastapi import APIRouter
from nba_api.stats.endpoints import playergamelog

router = APIRouter()


@router.get("/{type}")
def get_player_avg_totals(type: str):
    log = playergamelog.PlayerGameLog(
        player_id=1627759, season="2024-25", season_type_all_star="Regular Season"
    )
    df = log.get_data_frames()[0]

    # Columnas numéricas de estadísticas relevantes
    stats_columns = df.select_dtypes(include="number").columns.tolist()
    # Excluir columnas de ID o flags si no tienen sentido sumar
    stats_columns = [
        c for c in stats_columns if c not in ["Player_ID", "VIDEO_AVAILABLE"]
    ]

    # ? Totals
    # totals = df[["PTS", "REB", "AST", "STL", "BLK"]].sum()
    totals = df[stats_columns].sum()
    percent_columns = ["FG_PCT", "FG3_PCT", "FT_PCT"]  # columnas de porcentaje
    totals[percent_columns] = totals[percent_columns].round(2) / 100

    # ? Averages
    # averages = df[["PTS", "REB", "AST", "STL", "BLK"]].mean()
    averages = df[stats_columns].mean()
    percent_columns = ["FG_PCT", "FG3_PCT", "FT_PCT"]  # columnas de porcentaje
    # averages[percent_columns] = averages[percent_columns].round(2)
    averages[percent_columns] = averages[percent_columns].round(3)

    other_columns = [c for c in averages.index if c not in percent_columns]
    averages[other_columns] = averages[other_columns].round(1)
    # averages_rounded = averages.round(1)

    return {"totals": totals.to_dict(), "averages": averages.to_dict()}


def truncate(x, decimals=3):
    factor = 10**decimals
    return int(x * factor) / factor
