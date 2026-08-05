import sys
from typing import Any

import pygame

from ..level_generator.level_generator import level_generator
from .cheat_mode_window import render_cheat_mode
from .highscore_window import render_highscores
from .instructions_window import render_instruction
from .ui_helpers import BLACK, clicked, make_text, wants_to_quit

SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 1000


def menu(config: dict[str, Any]) -> None:
    """Render the main menu"""
    level_nb: int = 0
    num_level = config["number_level"]
    level = config["level_size"][level_nb]
    width = level["width"]
    height = level["height"]
    seed: int = config["seed"]
    infos: tuple[int, int, int, int, int] = (
        config["lives"],
        config["points_per_pacgum"],
        config["points_per_super_pacgum"],
        config["points_per_ghost"],
        config["level_max_time"],
        config["highscore_filename"]
    )

    cheat_settings: dict[str, Any] | None = None

    pygame.init()
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Main menu")
    pygame.font.init()
    font = pygame.font.SysFont("arial", 48)

    center_x = window.get_width() // 2
    clock = pygame.time.Clock()
    running: bool = True

    text_start_game, rect_start_game = make_text(
        font, "Start game", center=(center_x, window.get_height() // 6)
    )
    text_leaderboard, rect_leaderboard = make_text(
        font, "Leaderboard", center=(center_x, rect_start_game.bottom + 100)
    )
    text_instructions, rect_instructions = make_text(
        font, "Instructions", center=(center_x, rect_leaderboard.bottom + 100)
    )
    text_cheat_mode, rect_cheat_mode = make_text(
        font, "Cheat mode", center=(center_x, rect_instructions.bottom + 100)
    )
    text_exit, rect_exit = make_text(
        font, "Exit game", center=(center_x, rect_cheat_mode.bottom + 100)
    )

    while running:
        for event in pygame.event.get():
            if wants_to_quit(event):
                running = False
            elif clicked(event, rect_start_game):
                start_level = cheat_settings["level"] if cheat_settings else 0
                infos = ((cheat_settings["lives"],)
                         + infos[1:]) if cheat_settings else infos
                level_generator(width, height,
                                start_level, infos, window, seed)
                running = False
            elif clicked(event, rect_leaderboard):
                render_highscores(window, config["highscore_filename"])
            elif clicked(event, rect_instructions):
                render_instruction(window)
            elif clicked(event, rect_cheat_mode):
                cheat_settings = render_cheat_mode(window, num_level)
            elif clicked(event, rect_exit):
                running = False

        window.fill(BLACK)

        window.blit(text_start_game, rect_start_game)
        window.blit(text_leaderboard, rect_leaderboard)
        window.blit(text_instructions, rect_instructions)
        window.blit(text_cheat_mode, rect_cheat_mode)
        window.blit(text_exit, rect_exit)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()
