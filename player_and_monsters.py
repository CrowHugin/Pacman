from abc import ABC, abstractmethod
from typing import Any


class Mobs(ABC):
    def __init__(self,
                 status: str,
                 color: str,
                 coords: tuple[int, int]) -> None:
        self.status = status
        self.color = color
        self.coords = coords

    @abstractmethod
    def movements(self, coords: tuple[int, int]) -> None:
        pass

    @abstractmethod
    def eat(self, target: Any) -> None:
        pass


class Player(Mobs):
    def __init__(self,
                 nb_lives: int,
                 status: str,
                 color: str,
                 coords: tuple[int, int]) -> None:
        self.coords: tuple[int, int] = coords
        self.color = color
        self.nb_lives = nb_lives
        self.status = status

    def movements(self, coords: tuple[int, int]) -> None:
        # if x is pressed go to the Z direction
        pass

    def eat(self, target: Any) -> None:
        # if self.coords == target.coords:
        #     disable target visibility
        # target is pacgum or super pacgum
        pass


class Ghosts(Mobs):
    def __init__(self,
                 status: str,
                 color: str,
                 coords: tuple[int, int]) -> None:
        super().__init__(status, color, coords)

    def movements(self, coords: tuple[int, int]) -> None:
        # movements random dans la limites des cas possibles
        pass

    def eat(self, target: Any) -> None:
        # if self.coords == target.coords:
        #   player lives = -1
        #   player respawn on the center
        pass
