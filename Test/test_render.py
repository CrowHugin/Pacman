import pygame
import unittest
from unittest.mock import MagicMock
from UI.level_generator.level_generator import draw_maze


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

        mock_font = MagicMock()
        draw_maze(self.surface,
                  mock_maze,
                  self.cell_size,
                  None,
                  1,
                  mock_font,
                  1000,
                  None)

        pixel_color = self.surface.get_at((10, 0))[:3]
        self.assertEqual(pixel_color, (33, 33, 255))

    def test_pacgum(self) -> None:
        """
            Function to test if pacgums are drawn correctly
        """
        mock_maze = MagicMock()
        mock_maze.width = 1
        mock_maze.height = 1
        mock_maze.maze = [[0]]

        mock_case = MagicMock()
        mock_case.has_pacgum = True
        mock_case.has_super_pacgum = False
        mock_maze.cases = {(0, 0): mock_case}

        mock_font = MagicMock()

        self.surface.fill((0, 0, 0))

        draw_maze(self.surface,
                  mock_maze,
                  self.cell_size,
                  None,
                  1,
                  mock_font,
                  1000,
                  None)

        pixel_color = self.surface.get_at((10, 10))[:3]
        self.assertEqual(pixel_color, (240, 240, 240))

    def test_super_pacgum(self) -> None:
        """
            Function to test if super pacgums are drawn correctly
        """
        mock_maze = MagicMock()
        mock_maze.width = 1
        mock_maze.height = 1
        mock_maze.maze = [[0]]

        mock_case = MagicMock()
        mock_case.has_pacgum = False
        mock_case.has_super_pacgum = True
        mock_maze.cases = {(0, 0): mock_case}

        mock_font = MagicMock()

        self.surface.fill((0, 0, 0))

        draw_maze(self.surface,
                  mock_maze,
                  self.cell_size,
                  None,
                  1,
                  mock_font,
                  1000,
                  None)

        pixel_color = self.surface.get_at((10, 10))[:3]
        self.assertEqual(pixel_color, (255, 165, 0))
