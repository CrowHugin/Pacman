from parsing import load_game_config
from UI import menu

def run_highscore_menu() -> None:
    import pygame
    from UI.highscore_menu import render_highscores

    config = load_game_config("config.json")
    level = config["level_size"][0]
    width = level["width"]
    height = level["height"]
    pygame.init()
    pygame.display.set_caption("Highscores")
    pygame.font.init()

    CELL_SIZE = 30
    SCREEN_WIDTH = width * CELL_SIZE
    SCREEN_HEIGHT = height * CELL_SIZE

    window = pygame.display.set_mode((SCREEN_WIDTH,
                                      SCREEN_HEIGHT + (3 * CELL_SIZE)))
    render_highscores(window, config["highscore_filename"])


if __name__ == '__main__':
    menu(config=load_game_config("config.json"))
