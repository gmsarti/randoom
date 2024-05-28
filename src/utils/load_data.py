import json


def load_data(data_path):
    with open(data_path, "r") as file:
        data = json.load(file)

    return data
