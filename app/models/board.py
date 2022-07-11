from random import randint
from typing import List, Optional

from pydantic import BaseModel

from app.models.player import Players, PlayerUnit


class Patrimony(BaseModel):
    """Patrimony models"""

    location: int
    price: int = randint(30, 120)
    rent: int = randint(30, 120)
    owner: Optional[PlayerUnit]
    sold_out: bool = False


class BoardDetails(BaseModel):
    """Board details models"""

    winner: Optional[str]
    match: int = 0
    players: Players
    cards: List[Patrimony]


class ResultUnit(BaseModel):
    """Result unit models"""

    winner: str
    timeout: bool
    matches: int


class Result(BaseModel):
    """List result models"""

    __root__: List[ResultUnit] = []
