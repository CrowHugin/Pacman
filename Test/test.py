import enum
import unittest
from UI.Maze.Maze import Maze, Cell


class Test_level_Creation(unittest.TestCase):
    def setUp(self) -> None:
        self.width: int | None = 30
        self.height: int | None = 25
        self.seed: int | None = 42
        self.generator: Maze | None = Maze(self.width, self.height, self.seed)
        self.maze: list[list[str]] | None = self.generator.maze
        self.cases: dict[tuple[int, int], Cell] = {}

        if self.maze:
            for idx_row, row in enumerate(self.maze):
                for idx_col, item in enumerate(row):
                    self.cases[(idx_col, idx_row)] = Cell(idx_col,
                                                          idx_row,
                                                          int(item))

    def tearDown(self):
        self.width = None
        self.height = None
        self.seed = None
        self.maze = None
        self.cases = {}


    def test_cases_content(self):
        if self.maze:
            for ind_row, row in enumerate(self.maze):
                for ind_col, col in enumerate(row):
                    self.assertTrue(0 <= self.cases[(ind_col, ind_row)].content <= 15)
