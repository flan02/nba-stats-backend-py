# aux fc (parse data, format, filter, etc)

# utils.py


def calculate_shooting_percentages(totals: dict) -> dict:
    """
    Re calculate manually percentages (FG%, 3P%, FT%)
    from the totals of FGM/FGA, FG3M/FG3A, FTM/FTA.
    If attempts are 0, return 0.
    Returns the same modified dictionary.
    """
    try:
        fgm = totals.get("FGM", 0)
        fga = totals.get("FGA", 0)
        fg3m = totals.get("FG3M", 0)
        fg3a = totals.get("FG3A", 0)
        ftm = totals.get("FTM", 0)
        fta = totals.get("FTA", 0)

        totals["FG_PCT"] = round(fgm / fga, 3) if fga != 0 else 0
        totals["FG3_PCT"] = round(fg3m / fg3a, 3) if fg3a != 0 else 0
        totals["FT_PCT"] = round(ftm / fta, 3) if fta != 0 else 0

        for col in ["FG_PCT", "FG3_PCT", "FT_PCT"]:
            totals[col] = f"{totals[col]:.3f}"[1:]  # elimina el "0" adelante

        return totals

    except Exception as e:
        print(f"Error calculating shooting percentages: {e}")
        return totals
