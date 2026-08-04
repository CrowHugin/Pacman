import random
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from UI.Maze.Maze import Maze


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

    def _get_possible_moves(self, maze: "Maze") -> list[str]:
        DIRECTIONS = [
            (1, "UP"),
            (2, "RIGHT"),
            (4, "DOWN"),
            (8, "LEFT")
        ]
        content = maze.cases[self.coords].content
        return [direction for bit, direction in DIRECTIONS
                if not (content & bit)]

    def _get_weight(self,
                    level: int,
                    player: "Player",
                    moves: list[str]) -> list[int]:
        list_weight: list[int] = []
        weight_by_level: int = level * 10 + 5
        x, y = self.coords
        dx: int = player.coords[0] - x
        dy: int = player.coords[1] - y

        favorable_conditions = {
            "UP": dy < 0,
            "RIGHT": dx > 0,
            "DOWN": dy > 0,
            "LEFT": dx < 0,
        }
        if player.super:
            return [1 if favorable_conditions[move]
                    else weight_by_level for move in moves]
        else:
            return [
                weight_by_level if favorable_conditions[move] else 1
                for move in moves
            ]
        return list_weight

    def _movements(self, maze: "Maze", player: "Player", level: int) -> None:
        move_actions = {
            "UP": self.move_up,
            "RIGHT": self.move_right,
            "DOWN": self.move_down,
            "LEFT": self.move_left,
        }
        possible_moves: list[str] = self._get_possible_moves(maze)
        weight: list[int] = self._get_weight(level, player, possible_moves)

        if len(possible_moves) == 1:
            chosen_move = move_actions[possible_moves[0]]
        else:
            choice_random = random.choices(possible_moves, weight, k=1)[0]
            chosen_move = move_actions[choice_random]

        chosen_move(maze)

    def eat(self, target: Player) -> None:
        target.nb_lives -= 1
