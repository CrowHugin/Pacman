import sys
import pygame
from typing import Optional
from UI.Maze.Maze import Maze
from Characters.player_and_monsters import Player, Ghosts


def game_over(window: pygame.Surface,
              COLOR: tuple[int, int, int],
              font: pygame.font.Font) -> None:
    pygame.display.set_caption("GAME OVER")
    text_surface = font.render("GAME OVER", True, COLOR)
    text_rect = text_surface.get_rect(
        center=(window.get_width() // 2, window.get_height() // 2)
    )
    window.blit(text_surface, text_rect)


def win_screen(window: pygame.Surface,
               COLOR: tuple[int, int, int],
               font: pygame.font.Font,
               level: int) -> None:
    pygame.display.set_caption(f"Level - {level}")
    text_surface = font.render("CONGRATULATION", True, COLOR)
    text_rect = text_surface.get_rect(
        center=(window.get_width() // 2, window.get_height() // 2)
    )
    window.blit(text_surface, text_rect)


def infos_screen_left(window: pygame.Surface,
                      font_info: pygame.font.Font,
                      player: Player,
                      color: tuple[int, int, int],
                      size: tuple[int, int],
                      msg: str,
                      ) -> None:
    text_surface = font_info.render(msg, True, color)
    text_rect = text_surface.get_rect(
        bottomleft=size
    )
    window.blit(text_surface, text_rect)


def infos_screen_right(window: pygame.Surface,
                       font_info: pygame.font.Font,
                       player: Player,
                       color: tuple[int, int, int],
                       size: tuple[int, int],
                       msg: str,
                       ) -> None:
    text_surface = font_info.render(msg, True, color)
    text_rect = text_surface.get_rect(
        bottomright=size
    )
    window.blit(text_surface, text_rect)


def draw_maze(window: pygame.Surface,
              maze: "Maze",
              CELL_SIZE: int,
              player: Optional["Player"],
              level: int,
              font_info: pygame.font.Font,
              time: int,
              ghosts_tuple: Optional[tuple["Ghosts", ...]] = None,
              ) -> None:
    WHITE = (255, 255, 255)
    WALL_COLOR = (33, 33, 255)
    PLAYER_COLOR = (255, 255, 0)
    DOT_COLOR = (240, 240, 240)
    SUPER_DOT_COLOR = (255, 165, 0)
    WALL_THICKNESS = 2
    SCREEN_WIDTH = maze.width * CELL_SIZE
    SCREEN_HEIGHT = maze.height * CELL_SIZE

    window_width = window.get_width()
    window_height = window.get_height()
    offset_x = (window_width - SCREEN_WIDTH) // 2
    offset_y = (window_height - SCREEN_HEIGHT) // 2 - 40

    for row_idx in range(maze.height):
        for col_idx in range(maze.width):
            x = col_idx * CELL_SIZE + offset_x
            y = row_idx * CELL_SIZE + offset_y
            cell_value = maze.maze[row_idx][col_idx]

            left = x
            right = min(x + CELL_SIZE - 1, offset_x + SCREEN_WIDTH - 1)
            top = y
            bottom = min(y + CELL_SIZE - 1, offset_y + SCREEN_HEIGHT - 1)

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

            if maze.cases[(col_idx, row_idx)].has_pacgum and cell_value != 15:
                center_x = x + CELL_SIZE // 2
                center_y = y + CELL_SIZE // 2
                dot_radius = CELL_SIZE // 6
                pygame.draw.circle(window,
                                   DOT_COLOR,
                                   (center_x, center_y),
                                   dot_radius)

            if (maze.cases[(col_idx, row_idx)].has_super_pacgum
                    and cell_value != 15):
                center_x = x + CELL_SIZE // 2
                center_y = y + CELL_SIZE // 2
                dot_radius = CELL_SIZE // 6
                pygame.draw.circle(window,
                                   SUPER_DOT_COLOR,
                                   (center_x, center_y),
                                   dot_radius)

    if player:
        infos_screen_left(window,
                          font_info,
                          player,
                          WHITE,
                          (15,
                           offset_y + SCREEN_HEIGHT + (1 * CELL_SIZE) + 10),
                          f"Lives: {player.nb_lives}")

        infos_screen_left(window,
                          font_info,
                          player,
                          WHITE,
                          (15, offset_y + SCREEN_HEIGHT + (3 * CELL_SIZE)),
                          f"Score: {player.score}")

        infos_screen_right(window,
                           font_info,
                           player,
                           WHITE,
                           (window_width,
                            offset_y + SCREEN_HEIGHT + (1 * CELL_SIZE) + 10),
                           f"Current level: {level}",
                           )

        infos_screen_right(window,
                           font_info,
                           player,
                           WHITE,
                           (window_width,
                            offset_y + SCREEN_HEIGHT + (3 * CELL_SIZE)),
                           f"Time left: {time // 1000} s",
                           )

        if player.coords:
            player_x = player.coords[0] * CELL_SIZE + CELL_SIZE // 2 + offset_x
            player_y = player.coords[1] * CELL_SIZE + CELL_SIZE // 2 + offset_y
            # -5 to avoid drawing on walls
            radius = ((CELL_SIZE // 2) - 2) - 5

            pygame.draw.circle(window,
                               PLAYER_COLOR,
                               (player_x, player_y),
                               radius)

    if ghosts_tuple:
        for ghost in ghosts_tuple:
            if ghost.is_dead:
                continue
            x = ghost.coords[0] * CELL_SIZE + CELL_SIZE // 2 + offset_x
            y = ghost.coords[1] * CELL_SIZE + CELL_SIZE // 2 + offset_y
            radius = (CELL_SIZE // 2 - 2) - 5

            pygame.draw.circle(window,
                               ghost.color,
                               (x, y),
                               radius)


def check_pacgum(maze: "Maze") -> bool:
    for case in maze.cases.values():
        if case.has_pacgum:
            return False
    return True


def level_generator(width: int,
                    height: int,
                    level_number: int,
                    infos: tuple[int, int,  int, int, int],
                    window: pygame.Surface,
                    seed: int | None = None
                    ) -> None:
    player = Player(((width // 2) - 1, height // 2), infos[0])
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
    WHITE = (255, 255, 255)
    CELL_SIZE = 30
    BLACK = (0, 0, 0)

    pygame.init()
    pygame.display.set_caption(f"PAC-MAN - LEVEL {level_number}")
    pygame.font.init()
    font = pygame.font.SysFont("arial", 48)
    font_info = pygame.font.SysFont("arial", 30)

    clock = pygame.time.Clock()

    running: bool = True
    while running:
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        if player:
            if not player.is_dead:
                keys = pygame.key.get_pressed()
                if (current_time - player.last_moves >= player.move_delay):
                    content: int = maze.cases[player.coords].content
                    if keys[pygame.K_UP] and not (content & 1):
                        player.move_up(maze)
                        player.last_moves = current_time
                    elif keys[pygame.K_DOWN] and not (content & 4):
                        player.move_down(maze)
                        player.last_moves = current_time
                    elif keys[pygame.K_RIGHT] and not (content & 2):
                        player.move_right(maze)
                        player.last_moves = current_time
                    elif keys[pygame.K_LEFT] and not (content & 8):
                        player.move_left(maze)
                        player.last_moves = current_time
            if player.is_dead:
                if current_time - player.death_time >= 2000:
                    player.is_dead = False
                    player.coords = player.coords_spawn

            if player.coords != (-1, -1) and not player.is_dead:
                if player.super:
                    if current_time - player.super_time >= 3000:
                        player.super = False
                if maze.cases[(player.coords)].has_pacgum:
                    player.eat(infos[1])
                    maze.cases[(player.coords)].has_pacgum = False

                elif maze.cases[(player.coords)].has_super_pacgum:
                    player.eat(infos[2])
                    maze.cases[(player.coords)].has_super_pacgum = False
                    player.super = True
                    player.super_time = current_time

            if ghosts_tuple:
                for ghost in ghosts_tuple:
                    if ghost.is_dead:
                        if current_time - ghost.death_time >= 2000:
                            ghost.is_dead = False
                            ghost.coords = ghost.coords_spawn
                        else:
                            continue

                    if not ghost.is_dead:
                        if (current_time - ghost.last_moves_time
                                >= ghost.move_delay):
                            ghost._movements(maze, player, level_number)
                            ghost.last_moves_time = current_time
                        if ghost.coords == player.coords:
                            if not player.super:
                                ghost.eat(player)
                                player.is_dead = True
                                player.death_time = pygame.time.get_ticks()
                                player.coords = (-1, -2)
                            else:
                                player.eat(3)
                                ghost.is_dead = True
                                ghost.death_time = pygame.time.get_ticks()
                                ghost.coords = (-1, -1)

        time_limit = infos[4] * 1000
        window.fill(BLACK)
        if maze:
            if check_pacgum(maze):
                win_screen(window, WHITE, font, 1)
            elif (player and player.nb_lives <= 0) or (time_limit -
                                                       current_time <= 0):
                game_over(window, WHITE, font)
            else:
                draw_maze(window,
                          maze,
                          CELL_SIZE,
                          player,
                          level_number,
                          font_info,
                          time_limit - current_time,
                          ghosts_tuple)
        pygame.display.flip()
        clock.tick(60)

    sys.exit()
