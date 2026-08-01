import os
import unittest
from unittest.mock import MagicMock, patch

import pygame

from UI.main_menu import menu as menu_module

os.environ["SDL_VIDEODRIVER"] = "dummy"


BUTTON_SPACING = 115


def button_center_y(index: int) -> int:
    """index: 0=Start game, 1=Leaderboard,
    2=Instructions, 3=Cheat mode, 4=Exit."""
    return menu_module.SCREEN_HEIGHT // 6 + index * BUTTON_SPACING


def make_config() -> dict:
    return {
        "number_level": 3,
        "level_size": [{"width": 10, "height": 10}],
        "seed": 42,
        "highscore_filename": "scores.json",
        "lives": 3,
        "points_per_pacgum": 10,
        "points_per_super_pacgum": 50,
        "points_per_ghost": 200,
        "level_max_time": 60,
    }


class TestMenu(unittest.TestCase):
    def setUp(self) -> None:
        pygame.init()
        self.fake_font = MagicMock(spec=pygame.font.Font)
        self.fake_font.render.side_effect = (
            lambda text, aa, color: pygame.Surface((100, 30))
        )
        self.patches = {
            "sysfont": patch("pygame.font.SysFont",
                             return_value=self.fake_font),
            "clock": patch("pygame.time.Clock", return_value=MagicMock()),
            "level_generator": patch.object(menu_module, "level_generator"),
            "render_highscores": patch.object(menu_module,
                                              "render_highscores"),
            "render_instruction": patch.object(menu_module,
                                               "render_instruction"),
            "render_cheat_mode": patch.object(menu_module,
                                              "render_cheat_mode"),
            "sys_exit": patch("sys.exit"),
        }
        self.mocks = {name: p.start() for name, p in self.patches.items()}
        for p in self.patches.values():
            self.addCleanup(p.stop)

    def run_screen(self, event_batches: list[list]) -> None:
        with patch("pygame.event.get", side_effect=event_batches):
            menu_module.menu(make_config())

    def _click_at(self, y: int) -> pygame.event.Event:
        return pygame.event.Event(
            pygame.MOUSEBUTTONDOWN,
            button=1,
            pos=(menu_module.SCREEN_WIDTH // 2, y),
        )

    def test_start_game(
        self,
    ) -> None:
        start_click = self._click_at(button_center_y(0))
        self.run_screen([[start_click]])

        self.mocks["level_generator"].assert_called_once()
        _, _, start_level, *_ = self.mocks["level_generator"].call_args.args
        self.assertEqual(start_level, 0)

    def test_leaderboard_button_opens_highscores_screen(self) -> None:
        click = self._click_at(button_center_y(1))
        quit_event = pygame.event.Event(pygame.QUIT)
        self.run_screen([[click], [quit_event]])

        self.mocks["render_highscores"].assert_called_once()
        self.mocks["level_generator"].assert_not_called()

    def test_instructions_button_opens_instructions_screen(self) -> None:
        click = self._click_at(button_center_y(2))
        quit_event = pygame.event.Event(pygame.QUIT)
        self.run_screen([[click], [quit_event]])

        self.mocks["render_instruction"].assert_called_once()

    def test_exit_button_quits_without_starting_a_game(self) -> None:
        click = self._click_at(button_center_y(4))
        self.run_screen([[click]])

        self.mocks["level_generator"].assert_not_called()
        self.mocks["sys_exit"].assert_called_once()

    def test_escape_key_quits_the_menu(self) -> None:
        escape_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE)
        self.run_screen([[escape_event]])

        self.mocks["level_generator"].assert_not_called()
        self.mocks["sys_exit"].assert_called_once()

    def test_cheat_mode_level_is_used_when_starting_a_game(self) -> None:
        self.mocks["render_cheat_mode"].return_value = {
            "invincible": False,
            "ghost_freeze": False,
            "level": 2,
            "player_speed": 0.5,
            "extra_lives": 3,
        }
        cheat_click = self._click_at(button_center_y(3))
        start_click = self._click_at(button_center_y(0))
        self.run_screen([[cheat_click], [start_click]])

        self.mocks["render_cheat_mode"].assert_called_once()
        _, _, start_level, *_ = self.mocks["level_generator"].call_args.args
        self.assertEqual(start_level, 2)


if __name__ == "__main__":
    unittest.main()
