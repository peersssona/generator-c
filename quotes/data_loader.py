import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "quotes.json"


def load_quotes() -> list[str]:
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        return json.load(file)
