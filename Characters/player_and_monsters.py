from abc import ABC, abstractmethod
from typing import Any
import random


class Mobs(ABC):
    def __init__(self,
                 coords_spawn: tuple[int, int]) -> None:
        self.coords_spawn = coords_spawn
        self.coords = self.coords_spawn

    def move_up(self) -> None:
        x, y = self.coords
        self.coords = (x, y - 1)

    def move_right(self) -> None:
        x, y = self.coords
        self.coords = (x + 1, y)

    def move_down(self) -> None:
        x, y = self.coords
        self.coords = (x, y + 1)

    def move_left(self) -> None:
        x, y = self.coords
        self.coords = (x - 1, y)

    @abstractmethod
    def eat(self, target: Any) -> None:
        pass


class Player(Mobs):
    def __init__(self,
                 nb_lives: int,
                 speed: float,
                 coords_spawn: tuple[int, int]) -> None:
        super().__init__(coords_spawn)
        self.nb_lives = nb_lives

    def eat(self, target: Any) -> None:
        # if self.coords == target.coords:
        #     disable target visibility
        # target is pacgum or super pacgum
        pass


class Ghosts(Mobs):
    def __init__(self,
                 speed: float,
                 coords_spawn: tuple[int, int],
                 color: tuple[int, int, int]) -> None:
        super().__init__(coords_spawn)
        self.speed = speed
        self.color = color

    def movements(self) -> None:
        directions = [self.move_up,
                      self.move_down,
                      self.move_left,
                      self.move_right]
        random.choice(directions)()

    def eat(self, target: Any) -> None:
        # if self.coords == target.coords:
        #   player lives = -1
        #   player respawn on the center
        pass
