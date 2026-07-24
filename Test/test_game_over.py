import os
import pygame
import unittest
from UI.level_1.level_1 import game_over
from unittest.mock import MagicMock


os.environ["SDL_VIDEODRIVER"] = "dummy"


class TestGameOverRender(unittest.TestCase):
    def setUp(self) -> None:
        pygame.init()
        self.window = MagicMock(spec=pygame.Surface)
        self.window.get_width.return_value = 800
        self.window.get_height.return_value = 600

        self.font = MagicMock(spec=pygame.font.Font)
        self.text_surface_mock = MagicMock(spec=pygame.Surface)
        self.font.render.return_value = self.text_surface_mock

    def test_game_over_displays_text(self) -> None:
        BLACK = (0, 0, 0)
        game_over(self.window, BLACK, self.font)
        self.font.render.assert_called_with("GAME OVER", True, (255, 0, 0))
        self.window.blit.assert_called_once()
