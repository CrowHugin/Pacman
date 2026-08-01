import os
import unittest
from typing import Any
from unittest.mock import MagicMock, patch

import pygame

from UI.main_menu.cheat_mode_window import render_cheat_mode
from UI.main_menu.ui_helpers import WHITE

os.environ["SDL_VIDEODRIVER"] = "dummy"


FONT_SIZE = (200, 50)


def make_fake_font() -> MagicMock:
    fake_font = MagicMock(spec=pygame.font.Font)
    fake_font.render.side_effect = lambda text, aa, color: pygame.Surface(
        FONT_SIZE)
    return fake_font


class TestCheatMode(unittest.TestCase):
    def setUp(self) -> None:
        pygame.init()
        pygame.display.set_mode((800, 600))
        self.window = MagicMock(spec=pygame.Surface)
        self.window.get_width.return_value = 800
        self.window.get_height.return_value = 600

        self.fake_font = make_fake_font()

        font_patcher = patch("pygame.font.SysFont",
                             return_value=self.fake_font)
        font_patcher.start()
        self.addCleanup(font_patcher.stop)

        clock_patcher = patch("pygame.time.Clock", return_value=MagicMock())
        clock_patcher.start()
        self.addCleanup(clock_patcher.stop)

    def run_screen(self, event_batches: list[list[pygame.event.Event]]
                   ) -> dict[str, Any]:
        with patch("pygame.event.get", side_effect=event_batches):
            return render_cheat_mode(self.window, lvl_max=5)

    def test_quit_immediately_returns_default_settings(self) -> None:
        quit_event = pygame.event.Event(pygame.QUIT)
        settings = self.run_screen([[quit_event]])
        self.assertEqual(
            settings,
            {
                "invincible": False,
                "ghost_freeze": False,
                "level": 0,
                "player_speed": 0.5,
                "extra_lives": 3,
            },
        )

    def test_main_menu_button_closes_screen_without_changes(self) -> None:
        click = pygame.event.Event(
            pygame.MOUSEBUTTONDOWN, button=1, pos=(800 // 8, 600 // 10)
        )
        settings = self.run_screen([[click]])
        self.assertEqual(settings["level"], 0)

    def test_toggle_invincibility(self) -> None:
        click = pygame.event.Event(pygame.MOUSEBUTTONDOWN,
                                   button=1, pos=(400, 185))
        quit_event = pygame.event.Event(pygame.QUIT)
        settings = self.run_screen([[click], [quit_event]])
        self.assertTrue(settings["invincible"])
        self.fake_font.render.assert_any_call("Invincibility", True, WHITE)

    def test_toggle_ghost_freeze(self) -> None:
        click = pygame.event.Event(pygame.MOUSEBUTTONDOWN,
                                   button=1, pos=(400, 260))
        quit_event = pygame.event.Event(pygame.QUIT)
        settings = self.run_screen([[click], [quit_event]])
        self.assertTrue(settings["ghost_freeze"])

    def test_player_speed_increases_and_decreases(self) -> None:
        plus_pos = (500 + 50, 410)
        minus_pos = (300 - 50, 410)
        quit_event = pygame.event.Event(pygame.QUIT)
        plus_click = pygame.event.Event(pygame.MOUSEBUTTONDOWN,
                                        button=1, pos=plus_pos)
        minus_click = pygame.event.Event(pygame.MOUSEBUTTONDOWN,
                                         button=1, pos=minus_pos)

        settings = self.run_screen([[plus_click], [plus_click],
                                    [minus_click], [quit_event]])
        self.assertAlmostEqual(settings["player_speed"], 0.6)

    def test_extra_lives_regression_bug_minus_button_now_works(self) -> None:
        minus_pos = (300 - 50, 485)
        quit_event = pygame.event.Event(pygame.QUIT)
        click = pygame.event.Event(pygame.MOUSEBUTTONDOWN,
                                   button=1, pos=minus_pos)

        settings = self.run_screen([[click], [click],
                                    [click], [click], [quit_event]])
        # 3 -> 2 -> 1 -> 0, un 4e clic ne doit pas passer sous 0
        self.assertEqual(settings["extra_lives"], 0)

    def test_extra_lives_plus_button_increments(self) -> None:
        plus_pos = (500 + 50, 485)
        quit_event = pygame.event.Event(pygame.QUIT)
        click = pygame.event.Event(pygame.MOUSEBUTTONDOWN,
                                   button=1, pos=plus_pos)

        settings = self.run_screen([[click], [click], [quit_event]])
        self.assertEqual(settings["extra_lives"], 5)

    def test_level_increment_is_capped_at_lvl_max_minus_one(self) -> None:
        # Avant : "level <= lvl_max" permettait de dépasser le dernier
        # niveau valide (index 0..lvl_max-1). Corrigé en "< lvl_max - 1".
        plus_pos = (500 + 50, 335)  # rect_level.right + 50, rect_level.centery
        quit_event = pygame.event.Event(pygame.QUIT)
        click = pygame.event.Event(pygame.MOUSEBUTTONDOWN,
                                   button=1, pos=plus_pos)

        # lvl_max=5 -> dernier index valide = 4. On clique 6 fois.
        settings = self.run_screen([[click]] * 6 + [[quit_event]])
        self.assertEqual(settings["level"], 4)

    def test_level_decrement_cannot_go_below_zero(self) -> None:
        minus_pos = (300 - 50, 335)
        quit_event = pygame.event.Event(pygame.QUIT)
        click = pygame.event.Event(pygame.MOUSEBUTTONDOWN,
                                   button=1, pos=minus_pos)

        settings = self.run_screen([[click], [click], [quit_event]])
        self.assertEqual(settings["level"], 0)


if __name__ == "__main__":
    unittest.main()
