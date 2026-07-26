from parsing import load_game_config
from UI.Maze.Maze import Maze
from typing import Any
from UI.level_generator.level_generator import level_generator
from Characters.player_and_monsters import Player, Ghosts




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
        player = Player(((width // 2) - 1, height // 2), 3)
        red = Ghosts(1, (0, 0), (255, 0, 0))
        green = Ghosts(1, (0, height - 1), (0, 128, 0))
        blue = Ghosts(1, (width - 1, 0), (0, 0, 255))
        pink = Ghosts(1, (width - 1, height - 1), (255, 192, 203))
        ghosts_tuple: tuple[Ghosts, Ghosts, Ghosts, Ghosts] = (
            red,
            green,
            blue,
            pink
        )
        maze = Maze(width, height, seed)
        level_generator(maze, player, ghosts_tuple)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    run(config=load_game_config("config.json"))
