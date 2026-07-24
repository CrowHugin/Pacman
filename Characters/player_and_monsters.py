from abc import ABC, abstractmethod
from typing import Any


class Mobs(ABC):
    def __init__(self,
                 speed: float,
                 coords_spawn: tuple[int, int]) -> None:
        self.speed = speed
        self.coords_spawn = coords_spawn
        self.coords = self.coords_spawn

    @abstractmethod
    def movements(self, coords: tuple[int, int]) -> None:
        pass

    @abstractmethod
    def eat(self, target: Any) -> None:
        pass


class Player(Mobs):
    def __init__(self,
                 nb_lives: int,
                 speed: float,
                 coords_spawn: tuple[int, int]) -> None:
        super().__init__(speed, coords_spawn)
        self.nb_lives = nb_lives

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
                 speed: float,
                 coords_spawn: tuple[int, int],
                 color: str) -> None:
        super().__init__(speed, coords_spawn)
        self.color = color

    def movements(self, coords: tuple[int, int]) -> None:
        # movements random dans la limites des cas possibles
        pass

    def eat(self, target: Any) -> None:
        # if self.coords == target.coords:
        #   player lives = -1
        #   player respawn on the center
        pass
