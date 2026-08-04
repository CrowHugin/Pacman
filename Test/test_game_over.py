import os
import unittest
from unittest.mock import MagicMock, patch

import pygame

from UI.game_over_visual import game_over

os.environ["SDL_VIDEODRIVER"] = "dummy"


class TestGameOverRender(unittest.TestCase):
    def setUp(self) -> None:
        pygame.init()
        self.window = MagicMock(spec=pygame.Surface)
        self.window.get_width.return_value = 800
        self.window.get_height.return_value = 600

        self.font = MagicMock(spec=pygame.font.Font)
        self.font.render.return_value = MagicMock(spec=pygame.Surface)

        self.mock_score = 999
        self.mock_file = "mock_file.json"

        # Patches nécessaires pour que la boucle ne plante pas et se
        # termine (window est un mock, pas une vraie Surface)
        for target in (
            "UI.game_over_visual.pygame.draw.rect",
            "UI.game_over_visual.pygame.display.flip",
            "UI.game_over_visual.pygame.quit",
            "UI.game_over_visual.sys.exit",
        ):
            patcher = patch(target)
            patcher.start()
            self.addCleanup(patcher.stop)

    @patch("UI.game_over_visual.pygame.event.get")
    def test_game_over_displays_text(self, mock_event_get: MagicMock) -> None:
        """Test display GAME OVER text."""
        mock_event_get.return_value = [pygame.event.Event(pygame.QUIT)]

        game_over(self.window, (255, 255, 255), self.font,
                  False, self.mock_file, self.mock_score)

        self.font.render.assert_any_call("GAME OVER", True, (255, 0, 0))
        self.window.blit.assert_called()

    @patch("UI.game_over_visual.pygame.event.get")
    def test_game_over_win_displays_congrats(
        self, mock_event_get: MagicMock
    ) -> None:
        """Test display CONGRATULATION text."""
        mock_event_get.return_value = [pygame.event.Event(pygame.QUIT)]

        game_over(self.window, (255, 255, 255), self.font,
                  True, self.mock_file, self.mock_score)

        self.font.render.assert_any_call(
            "CONGRATULATION", True, (0, 255, 0))

    @patch("UI.game_over_visual.set_highscore")
    @patch("UI.game_over_visual.pygame.event.get")
    def test_enter_key_saves_highscore(
        self, mock_event_get: MagicMock, mock_set_highscore: MagicMock
    ) -> None:
        """Test if key enter pressed, the score is saved """
        enter_event = pygame.event.Event(
            pygame.KEYDOWN, key=pygame.K_RETURN)
        mock_event_get.side_effect = [
            [enter_event],
            [pygame.event.Event(pygame.QUIT)],
        ]

        game_over(self.window, (255, 255, 255), self.font,
                  False, self.mock_file, self.mock_score)

        mock_set_highscore.assert_called_once_with(
            self.mock_file, ("Joe", self.mock_score))

    @patch("UI.game_over_visual.pygame.event.get")
    def test_escape_key_closes_window(
        self, mock_event_get: MagicMock
    ) -> None:
        escape_event = pygame.event.Event(
            pygame.KEYDOWN, key=pygame.K_ESCAPE)
        mock_event_get.return_value = [escape_event]

        game_over(self.window, (255, 255, 255), self.font,
                  False, self.mock_file, self.mock_score)

    @patch("UI.game_over_visual.sys.exit")
    @patch("UI.game_over_visual.pygame.quit")
    @patch("UI.game_over_visual.pygame.display.flip")
    @patch("UI.game_over_visual.pygame.event.get")
    def test_backspace_removes_character(
        self, mock_event_get: MagicMock,
        mock_flip: MagicMock, mock_quit: MagicMock, mock_exit: MagicMock
    ) -> None:
        """Test to see if backspace removes character"""
        key_a = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_a, unicode="A")
        backspace = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_BACKSPACE,
                                       unicode="")
        quit_event = pygame.event.Event(pygame.QUIT)
        mock_event_get.side_effect = [[key_a], [backspace], [quit_event]]

        with patch("UI.game_over_visual.set_highscore"):
            game_over(self.window, (255, 255, 255), self.font,
                      False, self.mock_file, self.mock_score)

        rendered_texts = [c.args[0] for c in self.font.render.call_args_list]
        self.assertIn("JoeA", rendered_texts)
        self.assertIn("Joe", rendered_texts)
