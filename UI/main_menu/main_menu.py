import sys
from typing import Any

import pygame

from ..level_generator.level_generator import level_generator

SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 990
BLACK = (0, 0, 0)


def menu(config: dict[str, Any], game_progression: dict[str, Any]) -> None:

    level_nb: int = 0
    level = config["level_size"][level_nb]
    width = level["width"]
    height = level["height"]
    seed: int = config["seed"]
    infos: tuple[int, int, int, int, int, int] = (
        config["lives"],
        config["points_per_pacgum"],
        config["points_per_super_pacgum"],
        config["points_per_ghost"],
        config["level_max_time"],
        config["number_level"]
    )

    pygame.init()
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Main menu")
    pygame.font.init()
    font = pygame.font.SysFont("arial", 48)

    center_x = window.get_width() // 2
    clock = pygame.time.Clock()
    window.fill(BLACK)
    running: bool = True

    text_start_game = font.render("Start game", True, (255, 255, 255))
    text_rect_start_game = text_start_game.get_rect(
        center=(center_x, window.get_height() // 6)
    )

    text_leaderboard = font.render("Leaderboard", True, (255, 255, 255))
    text_rect_leaderboard = text_leaderboard.get_rect(
        center=(center_x, text_rect_start_game.bottom + 100)
    )

    text_instructions = font.render("Instructions", True, (255, 255, 255))
    text_rect_instructions = text_instructions.get_rect(
        center=(center_x, text_rect_leaderboard.bottom + 100)
    )

    text_cheat_mode = font.render("Cheat mode", True, (255, 255, 255))
    text_rect_cheat_mode = text_cheat_mode.get_rect(
        center=(center_x, text_rect_instructions.bottom + 100)
    )

    text_exit = font.render("Exit game", True, (255, 255, 255))
    text_rect_exit = text_exit.get_rect(
        center=(center_x, text_rect_cheat_mode.bottom + 100)
    )

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if text_rect_start_game.collidepoint(event.pos):
                    level_generator(width, height,
                                    0, infos, game_progression,
                                    window, config["highscore_filename"], seed)
                    running = False
                elif text_rect_leaderboard.collidepoint(event.pos):
                    print("Button leaderboard.")
                elif text_rect_instructions.collidepoint(event.pos):
                    print("Button instructions.")
                elif text_rect_cheat_mode.collidepoint(event.pos):
                    print("Button cheat mode.")
                elif text_rect_exit.collidepoint(event.pos):
                    print("Button exit.")

        window.fill(BLACK)

        window.blit(text_start_game, text_rect_start_game)
        window.blit(text_leaderboard, text_rect_leaderboard)
        window.blit(text_instructions, text_rect_instructions)
        window.blit(text_cheat_mode, text_rect_cheat_mode)
        window.blit(text_exit, text_rect_exit)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()
