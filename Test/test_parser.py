import unittest
from unittest.mock import mock_open, patch
from parsing.parser import (
    load_json_remove_comments,
    validate_level_size,
    validate_int_field,
    load_game_config,
)


class TestConfigParser(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="""
        {
            # Commentaire sur les pacgums
            "pacgum": 42,
            "lives": 3
        }
    """)
    def test_load_json_remove_comments_valid(self, mock_file) -> None:
        """Test parsing with a mock JSON file
        """
        data = load_json_remove_comments("mock_config.json")
        mock_file.assert_called_onced("mock_config.json")
        self.assertEqual(data, {"pacgum": 42, "lives": 3})

    def test_file_not_found(self) -> None:
        """Test if file not found, an empty dict is returned"""
        data = load_json_remove_comments("none_file.json")
        self.assertEqual(data, {})

    def test_level_size_valid(self) -> None:
        """Test validation a correct level size"""
        w, h, f = validate_level_size({"width": 10, "height": 10})
        self.assertEqual(w, 10)
        self.assertEqual(h, 10)
        self.assertFalse(f)

    def test_level_size_invalid(self) -> None:
        """Test for invalid value, the default value is returned"""
        w, h, f = validate_level_size({"width": 9, "height": 10})
        self.assertEqual(w, 15)
        self.assertEqual(h, 10)
        self.assertTrue(f)

    def test_int_field_valid(self) -> None:
        """Test a valid integer field"""
        data = {"lives": 5}
        val = validate_int_field("lives", data, def_val=3, min_val=1)
        self.assertEqual(val, 5)

    def test_int_field_below_min(self) -> None:
        """Test an incorrect integer field, default value returned"""
        data = {"lives": 2}
        val = validate_int_field("lives", data, def_val=3, min_val=1)
        self.assertEqual(val, 3)

    def test_int_field_boolean(self) -> None:
        """Test an boolean field, default value returned"""
        data = {"lives": True}
        val = validate_int_field("lives", data, def_val=3, min_val=1)
        self.assertEqual(val, 3)

    def test_load_game_config_default_values(self) -> None:
        """Test all default value are applied if missing file"""
        config = load_game_config("non_existent_config.json")
        self.assertEqual(config["lives"], 3)
        self.assertEqual(config["highscore_filename"], "score.json")
        self.assertEqual(config["pacgum"], 42)
        self.assertEqual(config["points_per_pacgum"], 20)
        self.assertEqual(config["points_per_super_pacgum"], 50)
        self.assertEqual(config["points_per_ghost"], 200)
        self.assertEqual(config["seed"], 42)
        self.assertEqual(config["level_max_time"], 60)
        self.assertEqual(config["number_level"], 10)
        for level in config["level_size"]:
            self.assertEqual(level, {"width": 10, "height": 10})

