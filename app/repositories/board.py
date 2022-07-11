from typing import List

from app.core.settings import default_settings
from app.models.board import BoardDetails, Patrimony
from app.models.player import Players, TypePlayer
from app.repositories.players import PlayerRepository


class BoardDetailRepository:
    """Board detail repository"""

    def __init__(self) -> None:
        self._properties_quantity = default_settings.PROPERTIES

    def _build_patrimonies(self) -> List[Patrimony]:
        """Function responsible to create patrimonies array
        Returns:
            List[Patrimony]: retunr a patrimonies array
        """
        result = [
            Patrimony(location=index)
            for index in range(self._properties_quantity)
        ]
        return result

    def _build_players(self) -> Players:
        """Function responsible to create a players instance
        Returns:
            Players: retunr a players instance
        """
        result = Players(
            impulsive=PlayerRepository(TypePlayer.impulsive),
            picky=PlayerRepository(TypePlayer.picky),
            prudent=PlayerRepository(TypePlayer.prudent),
            random=PlayerRepository(TypePlayer.random),
        )
        return result

    def get_details(self) -> BoardDetails:
        """Function responsible to generate all details for board service

        Returns:
            BoardDetails: return a board details
        """
        details = BoardDetails(
            players=self._build_players(),
            cards=self._build_patrimonies(),
        )
        return details
