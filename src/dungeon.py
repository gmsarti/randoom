from pathlib import Path
from random import choice, choices, randint

from create_npc import create_npc
from pydantic import BaseModel
from utils.load_data import load_data

project_root = Path(__file__).parent.parent
dungeons_path = project_root / "data" / "dungeon.json"


class Dungeon(BaseModel):
    """Represents a place in the wilderness."""

    wild_places_data: dict = load_data(dungeons_path)

    entrance: str
    form: str
    size: str
    layout: str
    ruination: str
    reward: str
    activity: str
    hazards: str
    trick: str
    number_of_rooms: int
    room: str
    room_details: str

    def __str__(self):
        return f"""
                This is a {self.size} dungeon. It's entrance is in {self.entrance}.
                It has {str(self.number_of_rooms)} rooms with the form of a {self.form} and a {self.layout} layout.
                It's ruinations is {self.ruination} and activity is {self.activity}.
                If you pass the {self.hazards} and {self.trick} you will get a {self.reward}.
                """


def create_dungeon(**kwargs):
    dungeons_data: dict = load_data(dungeons_path)

    entrance: str = choice(dungeons_data["dungeon_entrances"])
    form: str = choice(dungeons_data["dungeon_forms"])
    size: str = choices(["small", "medium", "big"], weights=[60, 30, 10], k=1)[0]
    layout: str = choice(dungeons_data["dungeon_layout"])
    ruination: str = choice(dungeons_data["dungeon_ruinations"])
    reward: str = choice(dungeons_data["dungeon_rewards"])
    activity: str = choice(dungeons_data["dungeon_activities"])
    hazards: str = choice(dungeons_data["dungeon_hazards"])
    trick: str = choice(dungeons_data["dungeon_tricks"])
    room: str = choice(dungeons_data["dungeon_rooms"])
    room_details: str = choice(dungeons_data["dungeon_room_details"])
    if size == "small":
        number_of_rooms: int = randint(3, 6)
    elif size == "medium":
        number_of_rooms: int = randint(5, 10)
    elif size == "big":
        number_of_rooms: int = randint(10, 30)
    else:
        number_of_rooms: int = randint(2, 50)

    # Overwrite defaults with provided keyword arguments
    data = {**locals(), **kwargs}  # Combine local variables and kwargs

    return Dungeon(**data)


def random_dungeon_npc():
    return create_npc(region="npc_underworld")


if __name__ == "__main__":
    place = create_dungeon()
    print(place)
    print(" ")
    npc = random_dungeon_npc()
    print(npc)
