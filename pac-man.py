from parsing import load_game_config
from typing import Any
from UI.level_generator.level_generator import level_generator


def check_value(width: int, height: int, seed: int | None) -> None:
    if width <= 0:
        raise ValueError("ERROR:\nWidth cannot be negative or equal to 0")
    elif height <= 0:
        raise ValueError("ERROR:\nHeight cannot be negative or equal to 0")


def run(config: dict[str, Any]) -> None:
    level = config["level_size"][0]
    width = level['width']
    height = level['height']
    seed: int = config["seed"]
    try:
        check_value(width, height, seed)
        level_generator(width, height, 0, seed)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    run(config=load_game_config("config.json"))
