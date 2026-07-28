import unittest
from unittest.mock import mock_open, patch
from score.highscores_manager import (get_highscores)


class TestHighscore(unittest.TestCase):
    mock_highscores_content = """
        {
            "Axel":100,
            "Kidax":20
        }
    """

    def test_get_highscores(self) -> None:
        """Test to get the highscores"""
        with patch(
                    'builtins.open',
                    new=mock_open(read_data=self.mock_highscores_content),
                    create=True
                ) as file_mock:
                    self.assertEqual(
                        get_highscores(file_mock),
                        {"Axel":100, "Kidax":20})
        

if __name__ == "__main__" : 
    unittest.main()