import os
from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    PROJECT_NAME: str = "MONOPOLY GAME"
    DESCRIPTION: str = "The game based challenge"
    VERSION: str = "1.0.0"
    BALANCE: int = os.getenv("BALANCE")
    SIMULATION: int = os.getenv("SIMULATION")
    ROUND_LIMIT: int = os.getenv("ROUND_LIMIT")
    PROPERTIES: int = os.getenv("PROPERTIES")
    CAPITAL_GAIN: int = os.getenv("CAPITAL_GAIN")

    class Config:
        case_sensitive = True


default_settings = Settings()
