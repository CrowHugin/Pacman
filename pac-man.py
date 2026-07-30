from parsing import load_game_config
from typing import Any
from UI.level_generator.level_generator import level_generator


def check_value(width: int, height: int, seed: int | None) -> None:
    if width <= 0:
        raise ValueError("ERROR:\nWidth cannot be negative or equal to 0")
    elif height <= 0:
        raise ValueError("ERROR:\nHeight cannot be negative or equal to 0")


def run(config: dict[str, Any]) -> None:
    level_nb: int = 0
    level = config["level_size"][level_nb]
    width = level['width']
    height = level['height']
    seed: int = config["seed"]
    infos: tuple[int, int, int, int, int] = (config["lives"],
                                             config["points_per_pacgum"],
                                             config["points_per_super_pacgum"],
                                             config["points_per_ghost"],
                                             config["level_max_time"])
    try:
        check_value(width, height, seed)
        level_generator(width, height, 0, infos, seed)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    run(config=load_game_config("config.json"))
