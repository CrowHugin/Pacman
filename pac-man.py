from parsing import validate_json 
from UI.Maze.Maze import Maze
from UI.level_1.level_1 import run_level_1

# Function to raise an error, will be changed when json parsing is done
def check_value(width: int, height: int, seed: int | None) -> None:
    if width <= 0:
        raise ValueError("ERROR:\nWidth cannot be negative or equal to 0")
    elif height <= 0:
        raise ValueError("ERROR:\nHeight cannot be negative or equal to 0")


def run() -> None:
    width: int = -30
    height: int = 25
    seed: int = 42
    try:
        check_value(width, height, seed)
        maze = Maze(width, height, seed)
        run_level_1(maze)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    config = validate_json("config.json")
    for level in config["level_size"]:
        width = level["width"]
        height = level["height"]
        
    print(f" longueur final de config level size{len(config["level_size"])}")
    print(f" le contenu final de level size {config["level_size"]}")
