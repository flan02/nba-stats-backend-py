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
