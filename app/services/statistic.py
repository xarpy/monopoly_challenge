from typing import Any, Dict, List

from app.models.board import Result
from app.models.player import TypePlayer


class Statistic:
    """Statistic service"""

    def __init__(self, data: Result) -> None:
        self._data = data.dict()["__root__"]

    def _get_total_timeout(self) -> int:
        """Function responsible to calculated total timeout value
        Returns:
            int: return a total value
        """
        total = 0
        for item in self._data:
            if item["timeout"]:
                total += 1
        return total

    def _translate_name(self, name: str) -> str:
        """Function responsible to translate behavior type for portuguese
        Args:
            name (str): received behavior name
        Returns:
            str: return behavior translated
        """
        result = None
        match name:
            case TypePlayer.impulsive.name:
                result = "impulsivo"
            case TypePlayer.picky.name:
                result = "exigente"
            case TypePlayer.prudent.name:
                result = "cauteloso"
            case TypePlayer.random.name:
                result = "aleatório"
        return result

    def _get_total_matches(self) -> int:
        """Function responsible to calculated total matches value
        Returns:
            int: return a total value
        """
        total = 0
        for item in self._data:
            total += item["matches"]
        return total

    def _count_behavior_victory(self) -> List[Dict[Any, Any]]:
        """Function responsible to count all victory registered
        and generated formatted data output
        Returns:
            List[Dict[Any, Any]]: return array data formatted
        """
        prudent = {"name": TypePlayer.prudent.name, "victory": 0}
        impulsive = {"name": TypePlayer.impulsive.name, "victory": 0}
        picky = {"name": TypePlayer.picky.name, "victory": 0}
        random = {"name": TypePlayer.random.name, "victory": 0}
        for item in self._data:
            match item["winner"]:
                case TypePlayer.impulsive.name:
                    impulsive["victory"] += 1
                case TypePlayer.picky.name:
                    picky["victory"] += 1
                case TypePlayer.prudent.name:
                    prudent["victory"] += 1
                case TypePlayer.random.name:
                    random["victory"] += 1
        return [impulsive, prudent, picky, random]

    def _get_bahavior_winner(self) -> str:
        """Function responsible to discover behavior winner
        Returns:
            str: return behavior name
        """
        count_list = self._count_behavior_victory()
        values = [item["victory"] for item in count_list]
        max_value = max(values)
        for behavior in count_list:
            if behavior["victory"] == max_value:
                return self._translate_name(behavior["name"])

    def _get_behavior_percentage(self) -> List[str]:
        """Function responsible to calculated behavior percentage
        Returns:
            List[str]: return array data with analysis
        """
        result = []
        count_list = self._count_behavior_victory()
        for item in count_list:
            name = self._translate_name(item["name"])
            percentage = (item["victory"] // len(self._data)) * 100
            result.append(f"{name}: {percentage}%")
        return result

    def show(self) -> None:
        """Function responsible to generated output analysis"""
        print(
            f"Quantas partidas terminam por time out (1000 rodadas): {self._get_total_timeout()}"
        )
        print(
            f"Quantos turnos em média demora uma partida: {self._get_total_matches()}"
        )
        print(
            f"Qual o comportamento que mais vence: {self._get_bahavior_winner()}"
        )
        print(
            f"Qual a porcentagem de vitórias por comportamento dos jogadores: {self._get_behavior_percentage()}"
        )
