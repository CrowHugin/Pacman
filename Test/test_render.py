import pygame
import unittest
from unittest.mock import MagicMock
from UI.level_1.level_1 import draw_maze


class TestMazeRender(unittest.TestCase):
    """
        Test if the draw function works correctly
    """
    def setUp(self) -> None:
        """
            Setup fonction to run before each test
        """
        pygame.init()
        self.surface = pygame.Surface((300, 300))
        self.cell_size: int = 20

    def test_draw_maze_pixels(self) -> None:
        """
            Function to test if the draw maze function does work
        """
        mock_maze = MagicMock()
        mock_maze.width = 1
        mock_maze.height = 1
        mock_maze.maze = [[1]]

        self.surface.fill((0, 0, 0))

        draw_maze(self.surface, mock_maze, self.cell_size, None, None)

        pixel_color = self.surface.get_at((10, 0))[:3]
        self.assertEqual(pixel_color, (33, 33, 255))

