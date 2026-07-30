import pygame
from score import get_highscores


def render_highscores(window: pygame.Surface, filename: str) -> None:
    pygame.display.set_caption("Highscores")
    BLACK = (0, 0, 0)
    font = pygame.font.SysFont("arial", 48)
    clock = pygame.time.Clock()
    center_x = window.get_width() // 2
    highscores = get_highscores(filename=filename)
    done = False

    #Todo trouver meilleur emplacement
    text_main_menu = font.render("Main Menu", True, (255, 255, 255))
    text_rect_main_menu = text_main_menu.get_rect(
        center=(window.get_width() // 10,window.get_height() // 10))

    while not done:
        pos_score = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if text_rect_main_menu.collidepoint(event.pos):
                        print('Button pressed.')

        window.fill(BLACK)
        text_surface = font.render("HIGHSCORES", True, (255, 255, 255))
        text_rect_highscore = text_surface.get_rect(
            center=(center_x, window.get_height() // 6))
        window.blit(text_surface, text_rect_highscore)
        window.blit(text_main_menu, text_rect_main_menu)

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
