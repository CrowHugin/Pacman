import sys
import pygame
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from UI.Maze.Maze import Maze


def create_level_1(maze: "Maze") -> None:
    CELL_SIZE = 20
    SCREEN_WIDTH = maze.width * CELL_SIZE
    SCREEN_HEIGHT = maze.height * CELL_SIZE
    pygame.init()
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("PAC-MAN - LEVEL 1")
    running: bool = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        window.fill((0, 0, 0))

        for row_idx in range(maze.height):
            for col_idx in range(maze.width):
                x = col_idx * CELL_SIZE
                y = row_idx * CELL_SIZE
                pygame.draw.rect(window, (240, 240, 240),
                                 (x, y, CELL_SIZE, CELL_SIZE))
        pygame.display.flip()
    pygame.quit()
    sys.exit()
