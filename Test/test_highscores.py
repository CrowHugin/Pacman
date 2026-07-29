import json
import unittest
from typing import Any
from score.highscores_manager import (
    get_highscores,
    set_highscore
)
from unittest.mock import mock_open, patch


class TestHighscore(unittest.TestCase):

    def setUp(self) -> None:
        self.mock_filename = "mock_score.json"
        self.mock_highscores_content = """
            {
                "Axel": 100,
                "Kidax": 20
            }
        """
        self.mock_new_scores_content = ("Joe", 200)

    # Simulate that the file exists
    @patch("pathlib.Path.is_file", return_value=True)
    def test_get_highscores(self, _: Any) -> None:
        """Test reading highscores mocked.
            _ is the mock argurment of @patch
        """
        with patch(
            "builtins.open",
            new=mock_open(read_data=self.mock_highscores_content),
            create=True,
        ):
            result = get_highscores(self.mock_filename)
            self.assertEqual(result, {"Axel": 100, "Kidax": 20})

    @patch("pathlib.Path.is_file", return_value=False)
    def test_get_highscores_file_not_found(self, _: Any) -> None:
        """Test returning empty dict when file does not exist."""
        result = get_highscores(self.mock_filename)
        self.assertEqual(result, {})

    @patch("pathlib.Path.is_file", return_value=True)
    def test_write_highscores(self, _: Any) -> None:
        """Test write highscores in file
        Path.is_file is mocked to return True so that get_highscores
        doesn't check the real filesystem.
        """
        with patch(
            "builtins.open",
            new=mock_open(read_data=self.mock_highscores_content),
            create=True,
        ) as mock_file:
            set_highscore(self.mock_filename, self.mock_new_scores_content)

            handle = mock_file()
            handle.write.assert_called_once_with(
                json.dumps(
                    {"Joe": 200, "Axel": 100, "Kidax": 20}, indent=4
                )
            )
