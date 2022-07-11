from random import randint

from app.core.settings import default_settings
from app.models.board import Patrimony
from app.models.player import PlayerUnit, TypePlayer


class PlayerRepository:
    """Player reponsitory"""

    def __init__(self, strategy_number: int, position: int = 0) -> None:
        self._position = position
        self._player = self._set_player(strategy_number)
        self._capital_round = default_settings.CAPITAL_GAIN

    @staticmethod
    def _set_player(strategy: int) -> PlayerUnit:
        """Function responsible create all players instance
        Args:
            strategy (int): received integer about type
        Returns:
            PlayerUnit: return Player instance
        """
        strategy_type = TypePlayer(strategy)
        player = PlayerUnit(strategy=strategy_type.name)
        return player

    @property
    def detail(self) -> PlayerUnit:
        """Player property"""
        return self._player

    @property
    def strategy(self) -> str:
        """Function responsible to get strategy information
        Returns:
            str: return strategy data
        """
        return self.detail.strategy

    @property
    def defeated(self) -> bool:
        """Function responsible to get defeated information
        Returns:
            bool: return a boolean about player defeated
        """
        return self.detail.defeated

    def _payments(self, patrimony: Patrimony, rent: bool = False) -> None:
        """Function responsible for all payment proccess, included rent payment
        and set condition about broken player!
        Args:
            patrimony (Patrimony): received patrimony instance
            rent (bool, optional): received bool about type proccess
        """
        if rent:
            self.detail.money -= patrimony.rent
            self._rent_received(patrimony)
        else:
            self.detail.money -= patrimony.price

        if not self.detail.money:
            self.detail.defeated = True

    def _rent_received(self, patrimony: Patrimony) -> None:
        """Function responsible to calculated rent received
        Args:
            patrimony (Patrimony): received patrimony instance
        """
        player_reference = patrimony.owner
        player_reference.money += patrimony.rent

    def _property_purchase(self, patrimony: Patrimony) -> None:
        """Function responsible to calculated purchase property depending
        on the type of player
        Args:
            patrimony (Patrimony): received patrimony instance
        """
        match self.detail.strategy:
            case TypePlayer.impulsive.name:
                self._payments(patrimony)
            case TypePlayer.picky.name:
                if patrimony.rent > 50:
                    self._payments(patrimony)
            case TypePlayer.prudent.name:
                reference_money = self.detail.money - patrimony.price
                if reference_money >= 80:
                    self._payments(patrimony)
            case TypePlayer.random.name:
                if randint(0, 1) > 0:
                    self._payments(patrimony)

    def capital_received(self) -> None:
        """Function responsible to calculated capital gained when
        complete match"""
        self.detail.money += self._capital_round

    def action_payment(self, patrimony: Patrimony) -> None:
        """Function responsible to decide which payment action execute
        Args:
             patrimony (Patrimony): received patrimony instance
        """
        if patrimony.owner:
            if self.detail != patrimony.owner:
                self._payments(patrimony, True)

        else:
            self._property_purchase(patrimony)
