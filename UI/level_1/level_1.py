import sys
import time
import pygame
from typing import TYPE_CHECKING, Optional


if TYPE_CHECKING:
    from UI.Maze.Maze import Maze
    from Characters.player_and_monsters import Player, Ghosts


def game_over(window: pygame.Surface,
              BLACK: tuple[int, int, int],
              font: pygame.font.Font) -> None:
    pygame.display.set_caption("GAME OVER")
    text_surface = font.render("GAME OVER", True, (255, 0, 0))
    text_rect = text_surface.get_rect(
       center=(window.get_width() // 2, window.get_height() // 2)
    )
    window.blit(text_surface, text_rect)


def draw_maze(window: pygame.Surface,
              maze: "Maze",
              CELL_SIZE: int,
              player_coords: Optional[tuple[int, int]],
              ghosts_tuple: Optional[tuple["Ghosts", ...]]
              ) -> None:
    WHITE = (255, 255, 255)
    WALL_COLOR = (33, 33, 255)
    PLAYER_COLOR = (255, 255, 0)
    WALL_THICKNESS = 2
    SCREEN_WIDTH = maze.width * CELL_SIZE
    SCREEN_HEIGHT = maze.height * CELL_SIZE

    for row_idx in range(maze.height):
        for col_idx in range(maze.width):
            x = col_idx * CELL_SIZE
            y = row_idx * CELL_SIZE
            cell_value = maze.maze[row_idx][col_idx]

            left = x
            right = min(x + CELL_SIZE - 1, SCREEN_WIDTH - 1)
            top = y
            bottom = min(y + CELL_SIZE - 1, SCREEN_HEIGHT - 1)

            top_left = (left, top)
            top_right = (right, top)
            bottom_left = (left, bottom)
            bottom_right = (right, bottom)

            if cell_value == 15:
                pygame.draw.rect(window,
                                 WHITE,
                                 (x, y, CELL_SIZE, CELL_SIZE)
                                 )
            # Bit 0 (1) -> Mur en HAUT
            if cell_value & 1:
                pygame.draw.line(window,
                                 WALL_COLOR,
                                 top_left,
                                 top_right,
                                 WALL_THICKNESS)

            # Bit 1 (2) -> Mur à DROITE
            if cell_value & 2:
                pygame.draw.line(window,
                                 WALL_COLOR,
                                 top_right,
                                 bottom_right,
                                 WALL_THICKNESS)

            # Bit 2 (4) -> Mur en BAS
            if cell_value & 4:
                pygame.draw.line(window,
                                 WALL_COLOR,
                                 bottom_left,
                                 bottom_right,
                                 WALL_THICKNESS)

            # Bit 3 (8) -> Mur à GAUCHE
            if cell_value & 8:
                pygame.draw.line(window,
                                 WALL_COLOR,
                                 top_left,
                                 bottom_left,
                                 WALL_THICKNESS)

    if player_coords:
        player_x = player_coords[0] * CELL_SIZE + CELL_SIZE // 2
        player_y = player_coords[1] * CELL_SIZE + CELL_SIZE // 2
        # -5 to avoid drawing on walls
        radius = (CELL_SIZE // 2 - 2) - 5

        pygame.draw.circle(window,
                           PLAYER_COLOR,
                           (player_x, player_y),
                           radius)

    if ghosts_tuple:
        for ghost in ghosts_tuple:
            x = ghost.coords[0] * CELL_SIZE + CELL_SIZE // 2
            y = ghost.coords[1] * CELL_SIZE + CELL_SIZE // 2
            radius = (CELL_SIZE // 2 - 2) - 5

            pygame.draw.circle(window,
                               ghost.color,
                               (x, y),
                               radius)


def run_level_1(maze: "Maze",
                player: Optional["Player"],
                ghost_tuple: Optional[tuple["Ghosts", ...]]
                ) -> None:
    CELL_SIZE = 30
    SCREEN_WIDTH = maze.width * CELL_SIZE
    SCREEN_HEIGHT = maze.height * CELL_SIZE
    BLACK = (0, 0, 0)

    pygame.init()
    window = pygame.display.set_mode((SCREEN_WIDTH,
                                      SCREEN_HEIGHT + (3 * CELL_SIZE)))
    pygame.display.set_caption("PAC-MAN - LEVEL 1")
    pygame.font.init()
    font = pygame.font.SysFont("arial", 48)

    clock = pygame.time.Clock()

    running: bool = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if player and ghost_tuple:
                    if event.key == pygame.K_UP:
                        player.move_up(maze)
                    elif event.key == pygame.K_DOWN:
                        player.move_down(maze)
                    elif event.key == pygame.K_RIGHT:
                        player.move_right(maze)
                    elif event.key == pygame.K_LEFT:
                        player.move_left(maze)

        if ghost_tuple and player:
            for ghost in ghost_tuple:
                ghost.movements(maze)
                if ghost.coords == player.coords:
                    ghost.eat(player)
        time.sleep(0.1)

        window.fill(BLACK)
        if player and ghost_tuple and maze:
            if player.nb_lives <= 0:
                game_over(window, BLACK, font)
                pygame.QUIT
            else:
                player_coords = player.coords if player else None
                draw_maze(window, maze, CELL_SIZE, player_coords, ghost_tuple)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
