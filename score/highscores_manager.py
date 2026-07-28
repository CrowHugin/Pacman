import json
from pathlib import Path
from typing import Dict


def get_highscores(filename: str) -> Dict[str, int]:
    my_file = Path(filename)
    if my_file.is_file():
        with open(my_file, "r", encoding="utf-8") as f:
            result: Dict[str, int] = json.load(f)
            return result
    else:
        return {}


# print(get_highscores("score.json"))
