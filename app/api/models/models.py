from typing import List
from pydantic import BaseModel
from typing import Optional


class Teams(BaseModel):
    id: int
    full_name: str
    abbreviation: str
    nickname: str
    city: str
    state: str
    year_founded: int


class Player(BaseModel):
    TeamID: int
    SEASON: str
    LeagueID: str
    PLAYER: str
    NICKNAME: str
    PLAYER_SLUG: str
    NUM: str
    POSITION: str
    HEIGHT: str
    WEIGHT: str
    BIRTH_DATE: str
    AGE: int
    EXP: str
    SCHOOL: Optional[str] = None
    PLAYER_ID: int
    HOW_ACQUIRED: str


class RosterResponse(BaseModel):
    team_id: Optional[int] = None
    count: Optional[int] = None
    players: List[Player]


class PlayerBoxScoreResponse(BaseModel):
    GAME_ID: str
    TEAM_ID: int
    TEAM_ABBREVIATION: str
    PLAYER_ID: int
    PLAYER_NAME: str
    MIN: Optional[str]  # puede ser None
    FGM: Optional[int]  # puede ser None
    FGA: Optional[int]
    FG_PCT: Optional[float]  # puede ser None
    FG3M: Optional[int]
    FG3A: Optional[int]
    FG3_PCT: Optional[float]
    FTM: Optional[int]
    FTA: Optional[int]
    FT_PCT: Optional[float]
    REB: Optional[int]
    AST: Optional[int]
    STL: Optional[int]
    BLK: Optional[int]
    TO: Optional[int]
    PF: Optional[int]
    PTS: Optional[int]
    PLUS_MINUS: Optional[int]


class LineupStatsResponse(BaseModel):
    GAME_ID: str
    TEAM_ID: int
    TEAM_NAME: str
    TEAM_ABBREVIATION: str
    TEAM_CITY: str
    STARTERS_BENCH: str
    MIN: str
    FGM: int
    FGA: int
    FG_PCT: float
    FG3M: int
    FG3A: int
    FG3_PCT: float
    FTM: int
    FTA: int
    FT_PCT: float
    OREB: int
    DREB: int
    REB: int
    AST: int
    STL: int
    BLK: int
    TO: int
    PF: int
    PTS: int


# {
# "GAME_ID": "0022400061",
# "TEAM_ID": 1610612738,
# "TEAM_NAME": "Celtics",
# "TEAM_ABBREVIATION": "BOS",
# "TEAM_CITY": "Boston",
# "STARTERS_BENCH": "Starters",
# "MIN": "143:26",
# "FGM": 40,
# "FGA": 65,
# "FG_PCT": 0.615,
# "FG3M": 26,
# "FG3A": 41,
# "FG3_PCT": 0.634,
# "FTM": 7,
# "FTA": 8,
# "FT_PCT": 0.875,
# "OREB": 4,
# "DREB": 17,
# "REB": 21,
# "AST": 24,
# "STL": 5,
# "BLK": 2,
# "TO": 2,
# "PF": 9,
# "PTS": 113
# }
