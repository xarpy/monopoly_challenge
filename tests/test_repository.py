import pytest

from app.core.settings import default_settings
from app.models.board import BoardDetails, Patrimony
from app.models.player import PlayerUnit
from app.repositories.board import BoardDetailRepository
from app.repositories.players import PlayerRepository


@pytest.fixture
def patrimony_acquired() -> Patrimony:
    player = PlayerUnit(strategy="prudent")
    return Patrimony(location=1, owner=player)


def test_board_details_repository():
    repositoy = BoardDetailRepository()
    assert type(repositoy.get_details()) == BoardDetails


def test_player_repository():
    repository = PlayerRepository(1)
    assert repository.strategy == "impulsive"
    assert type(repository.detail) == PlayerUnit
    assert repository.defeated is False


def test_player_repository_payment_action_patrimony_rented(patrimony_acquired):
    repository = PlayerRepository(1)
    repository.action_payment(patrimony_acquired)
    assert repository.detail.money != default_settings.BALANCE


def test_player_repository_capital_action():
    base_money = default_settings.BALANCE
    repository = PlayerRepository(1)
    repository.capital_received()
    assert (
        repository.detail.money - base_money == default_settings.CAPITAL_GAIN
    )
