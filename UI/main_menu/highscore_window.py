import pygame

from .ui_helpers import BLACK, WHITE, clicked
from .ui_helpers import make_main_menu_button, wants_to_quit

# from score import get_highscores

# Only here for the tests, will remove it


def get_highscores() -> dict[str, int]:
    return {}


def render_highscores(window: pygame.Surface, filename: str) -> None:
    """Render the leaderboard"""
    pygame.display.set_caption("Highscores")
    font = pygame.font.SysFont("arial", 48)
    clock = pygame.time.Clock()
    center_x = window.get_width() // 2
    done = False

    # highscores = get_highscores(filename=filename)
    highscores = {
        "Joe": 9999,
        "test": 4393,
        "pkpas": 4373,
        "blblbl": 20,
        "Josh": 10,
        "Jos": 10,
        "Jo": 10,
        "J": 10,
        "": 10,
        "c": 10,
    }

    text_main_menu, rect_main_menu = make_main_menu_button(window, font)
    text_title = font.render("HIGHSCORES", True, WHITE)
    rect_title = text_title.get_rect(
        center=(center_x, window.get_height() // 6))

    score_lines: list[tuple[pygame.Surface, pygame.Rect]] = []
    for i, (name, score) in enumerate(highscores.items()):
        surface = font.render(f"{name} : {score}", True, WHITE)
        rect = surface.get_rect(
            center=(center_x, window.get_height() // 4 + i * 50))
        score_lines.append((surface, rect))

    while not done:
        for event in pygame.event.get():
            if wants_to_quit(event) or clicked(event, rect_main_menu):
                done = True

        window.fill(BLACK)
        window.blit(text_title, rect_title)
        window.blit(text_main_menu, rect_main_menu)
        for surface, rect in score_lines:
            window.blit(surface, rect)

        pygame.display.flip()
        clock.tick(30)
