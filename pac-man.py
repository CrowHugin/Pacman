from parsing import validate_json
from UI.Maze.Maze import Maze
from UI.level_1.level_1 import run_level_1
from typing import Any
from Characters.player_and_monsters import Player, Ghosts

# Function to raise an error, will be changed when json parsing is done
def check_value(width: int, height: int, seed: int | None) -> None:
    if width <= 0:
        raise ValueError("ERROR:\nWidth cannot be negative or equal to 0")
    elif height <= 0:
        raise ValueError("ERROR:\nHeight cannot be negative or equal to 0")


def run(config: dict[str, Any]) -> None:
    level = config["level_size"][0]
    width = level['width']
    height = level['height']
    seed: int = config["seed"]
    try:
        check_value(width, height, seed)
        player = Player(3, 1, (0, 0))
        maze = Maze(width, height, seed)
        run_level_1(maze, player)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    config = validate_json("config.json")
    run(config=config)
