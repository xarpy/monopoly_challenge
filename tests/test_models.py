from app.core.settings import default_settings
from app.models.board import BoardDetails, Patrimony, Result, ResultUnit
from app.models.player import Players, PlayerUnit, TypePlayer


def test_player_type():
    assert TypePlayer.impulsive.name == "impulsive"
    assert TypePlayer.picky.name == "picky"
    assert TypePlayer.prudent.name == "prudent"
    assert TypePlayer.random.name == "random"


def test_player_unit():
    player = PlayerUnit(strategy="impulsive")
    assert player.money == default_settings.BALANCE
    assert type(player) == PlayerUnit


def test_player_set():
    players = Players()
    assert type(players) == Players


def test_board_patrimony():
    patrimony = Patrimony(location=1)
    assert type(patrimony) == Patrimony
    assert patrimony.owner is None
    assert patrimony.location == 1


def test_board_details():
    patrimony = Patrimony(location=1)
    board_details = BoardDetails(players=Players(), cards=[patrimony])
    assert type(board_details) == BoardDetails
    assert type(board_details.cards[0]) == Patrimony
    assert type(board_details.players) == Players
    assert board_details.match == 0


def test_board_result_unit():
    result = ResultUnit(winner="impulsive", timeout=False, matches=100)
    assert type(result) == ResultUnit


def test_board_result_list():
    result = ResultUnit(winner="impulsive", timeout=False, matches=100)
    list_result = Result(__root__=[result])
    assert type(list_result) == Result
    assert type(list_result.__root__[0]) == ResultUnit
