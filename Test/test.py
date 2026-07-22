import unittest
from levels.level_1 import Maze


class Test_level_Creation(unittest.TestCase):
    def setUp(self) -> None:
        self.maze = Maze(20, 20, 42)

    def test_first_case(self) -> None:
        self.assertEqual(self.maze.cases[(0, 0)].content, 9)

    def test_last_case(self) -> None:
        self.assertEqual(self.maze.cases[(19, 19)].content, 6)
