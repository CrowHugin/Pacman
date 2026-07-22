import os
from mazegenerator import MazeGenerator


def create_maze() -> list[list[str]]:
    mzgn = MazeGenerator(size=(20, 20), seed=42)
    maze: list[list[str]] = mzgn.maze
    return (maze)


def print_maze(maze: list[list[str]]) -> None:
    for items in maze:
        for item in items:
            print(f"{item:2d}", end=" ")
        print()


if __name__ == '__main__':
    os.system("clear")
    maze = create_maze()
    print_maze(maze)
