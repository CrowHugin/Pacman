import os
import unittest
from unittest.mock import MagicMock, patch

import pygame

from UI.main_menu.instructions_window import render_instruction

os.environ["SDL_VIDEODRIVER"] = "dummy"


class TestInstructionsWindow(unittest.TestCase):
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

    def test_renders_all_instruction(self) -> None:
        quit_event = pygame.event.Event(pygame.QUIT)
        with patch("pygame.event.get", return_value=[quit_event]):
            render_instruction(self.window)

        rendered_texts = [c.args[0] for c in
                          self.fake_font.render.call_args_list]
        self.assertIn("Main menu", rendered_texts)
        self.assertIn("Instruction", rendered_texts)
        self.assertIn("Use the arrow key to move freely in the maze",
                      rendered_texts)
        self.assertIn("you will be able to eat a ghost", rendered_texts)
        self.assertIn(
            "within the time limit or if you loose your 3 lives",
            rendered_texts
        )
        self.assertEqual(self.fake_font.render.call_count, 11)

    def test_quits_on_quit_event(self) -> None:
        quit_event = pygame.event.Event(pygame.QUIT)
        with patch("pygame.event.get", return_value=[quit_event]):
            render_instruction(self.window)


if __name__ == "__main__":
    unittest.main()
