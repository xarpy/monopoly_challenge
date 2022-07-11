from datetime import datetime
from random import randint
from typing import List, Optional

from app.core.settings import default_settings
from app.models.board import BoardDetails, ResultUnit
from app.models.player import Players, PlayerUnit
from app.repositories.board import BoardDetailRepository
from app.repositories.players import PlayerRepository


class GamePlayed:
    """Game played service"""

    def __init__(self) -> None:
        self._matches = 0
        self._limit = default_settings.ROUND_LIMIT
        self._winner = None
        self._details = self._build_details()
        self._start_time = datetime.now()
        self._cards_quantity = default_settings.PROPERTIES

    @staticmethod
    def _build_details() -> BoardDetails:
        """Static function responsible to generate board detail
        Returns:
            BoardDetails: return a board details
        """
        factory = BoardDetailRepository()
        return factory.get_details()

    @property
    def players(self) -> Players:
        """Players property
        Returns:
            Players: return a players instance
        """
        return self._details.players

    @property
    def winner(self) -> int:
        """Winner attribute property
        Returns:
            int: return a winner value
        """
        return self._winner

    @property
    def matches(self) -> int:
        """Matches attribute property
        Returns:
            int: return a matches value
        """
        return self._matches

    @matches.setter
    def matches(self, value: int) -> None:
        self._matches = value

    @winner.setter
    def winner(self, value: str) -> None:
        self._winner = value

    def _roll_dice(self) -> int:
        """Function responsible to roll the virtual dice
        Returns:
            int: returns an integer between 1 and 6
        """
        return randint(1, 6)

    def _move(self, player: PlayerRepository) -> int:
        """Function responsible to player move steps on the virtual board
        Args:
            player (PlayerRepository): received player respository instance
        Returns:
            int: return a steps moved
        """
        step = player.detail.position + self._roll_dice()
        if step >= self._cards_quantity:
            player.capital_received()
            step -= self._cards_quantity
            player.detail.matches = self._matches
        player.detail.position = step
        return step

    def list_players(self) -> List[PlayerUnit]:
        """Function responsible to generated players array
        Returns:
            List[PlayerUnit]: return a players array
        """
        result = []
        players = self.players.dict()
        for value in players.values():
            if value:
                result.append(value)
        return result

    def remove(self, player: PlayerRepository) -> None:
        """Function responsible for eliminating a player
        Args:
            player (PlayerRepository): received player respository
        """
        for item in self._details.cards:
            if item.owner == player.detail:
                item.owner = None
        setattr(self._details.players, player.strategy, None)

    def checking_winner(self, player: PlayerRepository) -> Optional[str]:
        """Function responsible for checking if the player has won
        Args:
            player (PlayerRepository): received player respository
        Returns:
            Optional[str]: return player type
        """
        if len(self.list_players()) == 1:
            return player.detail.strategy
        elif self._limit <= self._matches:
            winner = None
            money = 0
            for item in self.list_players():
                if item and item.detail.money > money:
                    winner = item
                    money = item.detail.money
            return winner.detail.strategy
        else:
            return None

    def play(self, player: PlayerRepository) -> None:
        """Function responsible to execute the game
        Args:
            player (PlayerRepository): received player respository
        """
        if not player.detail.defeated:
            patrimony = self._details.cards[self._move(player)]
            player.action_payment(patrimony)

    def final_result(self) -> ResultUnit:
        """Function responsible to generated results
        Returns:
            ResultUnit: return result instance
        """
        result = ResultUnit(
            winner=self.winner,
            timeout=self.matches > self._limit,
            matches=self.matches,
        )
        return result
