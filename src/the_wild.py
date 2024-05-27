import json
from pathlib import Path

project_root = Path(__file__).parent.parent
data_path = project_root / "data" / "wild.json"


def load_data(data_path=data_path):
    with open(data_path, "r") as file:
        data = json.load(file)

    return data
