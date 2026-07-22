import os
import sys
import pygame
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


def create_window(MAZE: list[list[str]]) -> None:
    CELL_SIZE = 40
    COLS = len(MAZE[0])
    ROWS = len(MAZE)
    SCREEN_WIDTH = COLS * CELL_SIZE
    SCREEN_HEIGHT = ROWS * CELL_SIZE
    pygame.init()
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("PAC-MAN")
    running: bool = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()    # Effacer l'écran en noir
        window.fill((0, 0, 0))

        for row_idx in range(ROWS):
            for col_idx in range(COLS):
                x = col_idx * CELL_SIZE
                y = row_idx * CELL_SIZE
                pygame.draw.rect(window, (240, 240, 240),
                                 (x, y, CELL_SIZE, CELL_SIZE))
        pygame.display.flip()
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    os.system("clear")
    maze = create_maze()
    create_window(maze)
