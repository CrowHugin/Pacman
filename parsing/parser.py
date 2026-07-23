import json
import logging
import copy
from typing import Any, Dict

DEFAULT_MAZE_CONFIG: Dict[str, Any] = {
    "highscore_filename": "score.json",
    "number_level": 10,
    "level_size": [
        {"width": 10, "height": 10},
        {"width": 10, "height": 10},
        {"width": 10, "height": 10},
        {"width": 10, "height": 10},
        {"width": 10, "height": 10},
        {"width": 10, "height": 10},
        {"width": 10, "height": 10},
        {"width": 10, "height": 10},
        {"width": 10, "height": 10},
        {"width": 10, "height": 10},
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
        try:
            res: Dict[str, Any] = json.loads(content)
            return res
        except ValueError as e:
            raise ValueError(f"ERROR {e}")
    except FileNotFoundError as e:
        raise FileNotFoundError(f"{e}")


def validate_level_size(level_size: Any) -> tuple[int, int, bool]:
    """ """
    default_width, default_height = 15, 15

    if not isinstance(level_size, dict):
        return default_width, default_height, True

    level_width = level_size.get("width")
    level_height = level_size.get("height")
    flag = False

    if isinstance(level_width, int) and 10 <= level_width <= 50:
        width = level_width
    else:
        width = default_width
        flag = True

    if isinstance(level_height, int) and  10 <= level_height <= 50:
        height = level_height
    else:
        height = default_height
        flag = True

    return width, height, flag


def validate_int_field(field: str, json_data: Dict[str, Any],
                       def_val: int, min_val: int) -> int:
    if field in json_data:
        val = json_data[field]
        if isinstance(val, int) and val > min_val:
            return val
        logging.warning(f"Invalid value for {field}, default value used")
    else:
        logging.warning(f"Value {field} not present, default value used")
    json_data[field] = def_val
    return def_val


def validate_json(file: str) -> dict[str, Any]:
    config = copy.deepcopy(DEFAULT_MAZE_CONFIG)
    try:
        json_data = json_with_comment(file)
        config["lives"] = validate_int_field(
            "lives", json_data, config["lives"], 2)

        config["pacgum"] = validate_int_field(
            "pacgum", json_data, config["pacgum"], 0)
        config["points_per_pacgum"] = validate_int_field(
            "points_per_pacgum",
            json_data, config["points_per_pacgum"], 0)
        config["points_per_super_pacgum"] = validate_int_field(
            "points_per_super_pacgum",
            json_data, config["points_per_super_pacgum"], 0)

        config["points_per_ghost"] = validate_int_field(
            "points_per_ghost", json_data, config["points_per_ghost"], 0)

        config["seed"] = validate_int_field(
            "seed", json_data, config["seed"], 0)

        config["level_max_time"] = validate_int_field(
            "level_max_time", json_data, config["level_max_time"], 59)

        config["number_level"] = validate_int_field(
            "number_level", json_data, config["number_level"], 9)

        if "level_size" in json_data:
            list_level = json_data["level_size"]
            count_level = json_data["number_level"]
            if isinstance(list_level, list):
                len_list = len(list_level)
                if len_list < count_level:
                    for i in range(len_list, count_level - 1):
                        config["level_size"].append(
                            DEFAULT_MAZE_CONFIG["level_size"][0])
                elif len_list > count_level:
                    list_level = list_level[:count_level]
                for i, level in enumerate(list_level):
                    width, height, flag = validate_level_size(level)
                    config["level_size"][i]["width"] = width
                    config["level_size"][i]["height"] = height
                    if flag:
                        logging.warning("Invalid level size value, "
                                        "default value used")
            else:
                logging.warning("Invalid level size value, "
                                "default value used")
    except (ValueError,FileNotFoundError) as e:
        logging.warning(f"{e}, default value used")
    return config


text = validate_json("config.json")
for line in text:
    print(f"{line} : {text[line]}\n")
