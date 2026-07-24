import unittest
from UI.Maze.Maze import Cell
from unittest.mock import MagicMock
from Characters.player_and_monsters import Player, Ghosts


class TestCharactersCreation(unittest.TestCase):
    def test_player_initialization(self) -> None:
        player = Player((5, 5))
        self.assertEqual(player.coords, (5, 5))
        self.assertEqual(player.nb_lives, 3)

    def test_ghost_initialization(self) -> None:
        ghost = Ghosts(speed=1, coords_spawn=(10, 10), color=(255, 0, 0))
        self.assertEqual(ghost.coords, (10, 10))
        self.assertEqual(ghost.color, (255, 0, 0))


class TestPlayerMovement(unittest.TestCase):
    def setUp(self) -> None:
        self.player = Player((1, 1))
        self.mock_maze = MagicMock()

        grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.mock_maze.maze = grid
        self.mock_maze.width = 3
        self.mock_maze.height = 3
        self.mock_maze.cases = {}
        for idx_row, row in enumerate(grid):
            for idx_col, item in enumerate(row):
                self.mock_maze.cases[(idx_col, idx_row)] = Cell(
                    idx_col,
                    idx_row,
                    item
                )

    def test_move_right_success(self) -> None:
        self.player.move_right(self.mock_maze)
        self.assertEqual(self.player.coords, (2, 1))

    def test_move_up_blocked_by_wall(self) -> None:
        self.mock_maze.cases[(1, 1)].content = 1
        self.player.move_up(self.mock_maze)
        self.assertEqual(self.player.coords, (1, 1))


class TestInteractions(unittest.TestCase):
    def setUp(self) -> None:
        self.player = Player((1, 1))
        self.ghost = Ghosts(speed=1, coords_spawn=(1, 1), color=(255, 0, 0))

    def test_ghost_eats_player(self) -> None:
        initial_lives = self.player.nb_lives
        self.ghost.eat(self.player)
        self.assertEqual(self.player.nb_lives, initial_lives - 1)
        self.assertEqual(self.player.coords, (1, 1))
