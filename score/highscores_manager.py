import json
from pathlib import Path


def get_highscores(filename: str) -> dict[str,int]:
    my_file = Path(filename)
    if my_file.is_file():
        with open(my_file, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {}


print(get_highscores("score.json"))
