from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel

from app.core.settings import default_settings


class TypePlayer(Enum):
    """Types of players enum"""

    impulsive = 1
    picky = 2
    prudent = 3
    random = 4


class PlayerUnit(BaseModel):
    """Player unit model"""

    position: int = 0
    money: int = default_settings.BALANCE
    defeated: bool = False
    properties: int = 0
    strategy: str
    matches: int = 0


class Players(BaseModel):
    """Players model"""

    impulsive: Optional[Any]
    picky: Optional[Any]
    prudent: Optional[Any]
    random: Optional[Any]
