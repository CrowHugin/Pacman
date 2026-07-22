import json
import logging
from typing import Any, Dict

DEFAULT_MAZE_CONFIG = {
    "highscore_filename": "score.json",
    "number_level": 2,
    "level_size": [
        {"width": 10, "height": 10},
        {"width": 10, "height": 10}
    ],
    "lives": 3,
    "pacgum": 42,
    "points_per_pacgum": 20,
    "points_per_super_pacgum": 50,
    "points_per_ghost": 200,
    "seed": 42,
    "level_max_time": 90
}


def json_with_comment(file: str) -> Dict[str, Any]:
    json_stripped = []
    try:
        with open(file, "r") as f:
            for line in f:
                line_stripped = line.strip()
                if line_stripped.startswith("#"):
                    continue
                json_stripped.append(line_stripped)
        content = "".join(json_stripped)
        if not content:
            return {}
        return json.loads(content)
    except FileNotFoundError as e:
        logging.warning(f"can't read the file {file}")


def validate_json(file: str) -> list[str, Any]:
    json_data = json_with_comment(file)
    config = DEFAULT_MAZE_CONFIG.copy()

    def check_level_sive(level_size: dict) -> tuple[int,int, bool]:
        default_height = 15
        default_width = 15
        flag = False
        if not isinstance(level_size, dict):
            return default_width, default_height
        if "width" in level_size and "height" in level_size:
            level_width = level_size.get("width")
            level_height = level_size.get("height")
            if not isinstance(level_width,int) and level_width < 10:
                level_width = default_width
                flag = True
            if not isinstance(level_height, int) and level_height < 10:
                level_height = default_height 
                flag = True
        return level_width, level_height,flag
    
    if "lives" in json_data:
        val = json_data["lives"]
        if isinstance(val, int) and val > 0:
            config["lives"] = val
        else:
            logging.warning(f"Invalid value for lives, default value used")

    if "pacgum" in json_data:
        val = json_data["pacgum"]
        if isinstance(val, int) and val > 0:
            config["pacgum"] = val
        else:
            logging.warning(f"Invalid value for pacgum, default value used")

    if "points_per_pacgum" in json_data:
        val = json_data["points_per_pacgum"]
        if isinstance(val, int) and val > 0:
            config["points_per_pacgum"] = val
        else:
            logging.warning(f"Invalid value for points per pacgum,"
                            f"default value used")
    if "points_per_super_pacgum" in json_data:
        val = json_data["points_per_super_pacgum"]
        if isinstance(val, int) and val > 0:
            config["points_per_super_pacgum"] = val
        else:
            logging.warning(f"Invalid value for points per super pacgum,"
                            f"default value used")
    if "points_per_ghost" in json_data:
        val = json_data["points_per_ghost"]
        if isinstance(val, int) and val > 0:
            config["points_per_ghost"] = val
        else:
            logging.warning(f"Invalid value for points per ghost,"
                            f"default value used")

    if "seed" in json_data:
        val = json_data["seed"]
        if isinstance(val, int) and val > 0:
            config["seed"] = val
        else:
            logging.warning(f"Invalid value for seed,"
                            f"default value used")

    if "level_max_time" in json_data:
        val = json_data["level_max_time"]
        if isinstance(val, int) and val > 60:
            config["level_max_time"] = val
        else:
            logging.warning(f"Invalid value for points level max time,"
                            f"default value used")

    if "highscore_filename" in json_data:
        val = json_data["highscore_filename"]
        if isinstance(val, str) and val.endswith(".json"):
            config["highscore_filename"] = val
        else:
            logging.warning(f"Invalid value for highscore filename,"
                            f"default value used")

    if "number_level" in json_data:
        val = json_data["number_level"]
        if isinstance(val, int) and val >= 10:
            config["number_level"] = val
        else:
            logging.warning(f"Invalid value for number level,"
                            f"default value used")

    if "level_size" in json_data:
        list_level = json_data["level_size"]
        len_list = len(list_level)
        # if len_list == config["number_level"]:
        if len_list == 2:
            if isinstance(list_level, list):
                for level in list_level:
                    width,height,flag = check_level_sive(level)
                    print(level["width"])
                # if all(isinstance(value, dict) for value in list_level):
                #     for level in list_level:
                #         for val in level:
                #             if (isinstance(val, str) and (val == "width" or val == "height")
                #                and isinstance(level[val], int) and level[val] > 0):

        else:
            logging.warning(f"Invalid level size value,"
                            f"default value used")

    return config


text = validate_json("config.json")
