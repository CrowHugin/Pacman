from UI.Maze.Maze import Maze
from UI.level_1.level_1 import create_level_1


if __name__ == '__main__':
    maze = Maze(30, 25, 42)
    create_level_1(maze)
