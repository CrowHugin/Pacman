import unittest
from score.highscores_manager import (get_highscores)
from unittest.mock import MagicMock, mock_open, patch


class TestHighscore(unittest.TestCase):

    def setUp(self) -> None:
        self.mock_filename = "mock_score.json"
        self.mock_highscores_content = """
            {
                "Axel": 100,
                "Kidax": 20
            }
        """

    @patch("pathlib.Path.is_file", return_value=True)
    def test_get_highscores(self, mock_is_file: MagicMock) -> None:
        """Test reading highscores with both open and Path.is_file mocked."""
        with patch(
            "builtins.open",
            new=mock_open(read_data=self.mock_highscores_content),
            create=True,
        ):
            result = get_highscores(self.mock_filename)
            self.assertEqual(result, {"Axel": 100, "Kidax": 20})

    @patch("pathlib.Path.is_file", return_value=False)
    def test_get_highscores_file_not_found(self,
                                           mock_is_file: MagicMock) -> None:
        """Test returning empty dict when file does not exist."""
        result = get_highscores(self.mock_filename)
        self.assertEqual(result, {})
