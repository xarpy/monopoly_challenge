from app.core.settings import default_settings
from app.models.board import Result
from app.services.game import GamePlayed
from app.services.statistic import Statistic


def execute():
    """Method responsible to compile the project"""
    results = Result()
    for i in range(default_settings.SIMULATION):
        game = GamePlayed()
        while not game.winner:
            for player in game.list_players():
                if player.defeated:
                    game.remove(player)
                winner = game.checking_winner(player)
                if winner:
                    game.winner = winner
                    break
                game.play(player)
            game.matches += 1
        results.__root__.append(game.final_result())
    stats = Statistic(results)
    stats.show()
