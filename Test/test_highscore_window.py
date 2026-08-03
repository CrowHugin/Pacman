import os
import unittest
from unittest.mock import MagicMock, patch

import pygame

from UI.main_menu.highscore_window import render_highscores

os.environ["SDL_VIDEODRIVER"] = "dummy"


class TestHighscoreWindow(unittest.TestCase):
    def setUp(self) -> None:
        pygame.init()
        pygame.display.set_mode((800, 600))
        self.window = MagicMock(spec=pygame.Surface)
        self.window.get_width.return_value = 800
        self.window.get_height.return_value = 600

        self.fake_font = MagicMock(spec=pygame.font.Font)
        self.fake_font.render.side_effect = (
            lambda text, aa, color: pygame.Surface((100, 30))
        )
        self.addCleanup(
            patch("pygame.font.SysFont",
                  return_value=self.fake_font).start().stop
        )
        self.addCleanup(patch("pygame.time.Clock",
                              return_value=MagicMock()).start().stop)

    def test_renders_score_(self) -> None:
        quit_event = pygame.event.Event(pygame.QUIT)
        with patch("pygame.event.get", return_value=[quit_event]):
            render_highscores(self.window, "mock_highscores.json")

        rendered_texts = [c.args[0] for c in
                          self.fake_font.render.call_args_list]
        self.assertIn("HIGHSCORES", rendered_texts)
        self.assertIn("Main menu", rendered_texts)
        self.assertIn("Joe : 9999", rendered_texts)
        self.assertIn("test : 4393", rendered_texts)
        self.assertEqual(self.fake_font.render.call_count, 12)

    def test_quits_on_escape_key(self) -> None:
        escape_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE)
        with patch("pygame.event.get", return_value=[escape_event]):
            render_highscores(self.window, "mock.json")

    def test_quits_main_menu_button_clicked(self) -> None:
        click = pygame.event.Event(
            pygame.MOUSEBUTTONDOWN, button=1, pos=(800 // 8, 600 // 10)
        )
        with patch("pygame.event.get", return_value=[click]):
            render_highscores(self.window, "mock.json")
