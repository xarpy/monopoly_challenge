import pytest

from app.models.board import Result, ResultUnit
from app.models.player import Players, TypePlayer
from app.services.game import GamePlayed
from app.services.statistic import Statistic


@pytest.fixture
def list_results() -> Result:
    results = Result()
    for i in range(4):
        index = i + 1
        player_type = TypePlayer(index)
        unit = ResultUnit(winner=player_type.name, timeout=True, matches=index)
        results.__root__.append(unit)
    return results


def test_gameplayed_service():
    service = GamePlayed()
    assert type(service.players) == Players


def test_statistic_service(list_results):
    service = Statistic(list_results)
    assert type(service._data) == list
