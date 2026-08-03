import random
from typing import Any
from UI.Maze.Maze import Maze
from abc import ABC, abstractmethod


class Mobs(ABC):
    def __init__(self,
                 coords_spawn: tuple[int, int]) -> None:
        self.coords_spawn = coords_spawn
        self.coords = self.coords_spawn
        self.death_time: int = 0
        self.is_dead: bool = False

    def move_up(self, maze: "Maze") -> None:
        x, y = self.coords
        self.coords = (x, y - 1)

    def move_right(self, maze: "Maze") -> None:
        x, y = self.coords
        self.coords = (x + 1, y)

    def move_down(self, maze: "Maze") -> None:
        x, y = self.coords
        self.coords = (x, y + 1)

    def move_left(self, maze: "Maze") -> None:
        x, y = self.coords
        self.coords = (x - 1, y)

    @abstractmethod
    def eat(self, target: Any) -> None:
        pass


class Player(Mobs):
    def __init__(self,
                 coords_spawn: tuple[int, int],
                 nb_lives: int = 3) -> None:
        super().__init__(coords_spawn)
        self.nb_lives = nb_lives
        self.score = -20
        self.super: bool = False
        self.super_time: int = 0

    def eat(self, score: int) -> None:
        self.score += score


class Ghosts(Mobs):
    def __init__(self,
                 speed: float,
                 coords_spawn: tuple[int, int],
                 color: tuple[int, int, int]) -> None:
        super().__init__(coords_spawn)
        self.speed = speed
        self.color = color
        self.last_moves_time: int = 0
        self.move_delay = 300

    def movements(self, maze: "Maze", player: "Player", level: int) -> None:
        directions = []
        weight: list[int] = []
        x, y = self.coords
        dx: int = player.coords[0] - x
        dy: int = player.coords[1] - y

        safe_level = max(1, level)
        weight_by_level: int = safe_level * 10
        
        if (x, y) in maze.cases:
            if not maze.cases[(x, y)].content & 1:
                directions.append(self.move_up)
                weight.append(weight_by_level if dy < 0 else 1)

            if not maze.cases[(x, y)].content & 2:
                directions.append(self.move_right)
                weight.append(weight_by_level if dx > 0 else 1)

            if not maze.cases[(x, y)].content & 4:
                directions.append(self.move_down)
                weight.append(weight_by_level if dy > 0 else 1)

            if not maze.cases[(x, y)].content & 8:
                directions.append(self.move_left)
                weight.append(weight_by_level if dx < 0 else 1)

        if directions:
            chosen_move = random.choices(directions, weight, k=1)[0]
            chosen_move(maze)

    def eat(self, target: Player) -> None:
        target.nb_lives -= 1
