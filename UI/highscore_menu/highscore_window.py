import sys
import time
import pygame
from typing import TYPE_CHECKING, Optional
from score import get_highscores


def render_highscores(filename: str, width, height) -> None:
    pygame.init()
    pygame.display.set_caption("Highscores")
    pygame.font.init()

    CELL_SIZE = 30
    SCREEN_WIDTH = width * CELL_SIZE
    SCREEN_HEIGHT = height * CELL_SIZE
    BLACK = (0, 0, 0)

    font = pygame.font.SysFont("arial", 48)

    clock = pygame.time.Clock()

    window = pygame.display.set_mode((SCREEN_WIDTH,
                                      SCREEN_HEIGHT + (3 * CELL_SIZE)))
    center_x = window.get_width() // 2
    highscores = get_highscores(filename=filename)
    done = False

    while not done:
        pos_score = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
        window.fill(BLACK)

        text_surface = font.render("HIGHSCORES", True, (255, 0, 0))
        text_rect_highscore = text_surface.get_rect(
            center=(center_x, window.get_height() // 6))
        window.blit(text_surface, text_rect_highscore)

        for i, (name, score) in enumerate(highscores.items()):
            text_score = font.render(
                f"{name} : {score}", True, (255, 255, 255))
            pos_score = i * 50
            text_rect_scores = text_score.get_rect(
                center=(center_x, (window.get_height() // 4) +
                        pos_score))
            window.blit(text_score, text_rect_scores)

        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
    exit()
