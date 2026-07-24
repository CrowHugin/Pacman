from UI.Maze.Maze import Maze
from UI.level_1.level_1 import run_level_1
from Characters.player_and_monsters import Player, Ghosts


# Function to raise an error, will be changed when json parsing is done
def check_value(width: int, height: int, seed: int | None) -> None:
    if width <= 0:
        raise ValueError("ERROR:\nWidth cannot be negative or equal to 0")
    elif height <= 0:
        raise ValueError("ERROR:\nHeight cannot be negative or equal to 0")


def run() -> None:
    width: int = 30
    height: int = 25
    seed: int = 42
    try:
        check_value(width, height, seed)
        player = Player(3, 1, ((width // 2) - 1, height // 2))
        maze = Maze(width, height, seed)
        run_level_1(maze, player)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    run()
