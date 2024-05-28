from pathlib import Path
from random import choice
from typing import Optional

from create_npc import create_npc
from pydantic import BaseModel
from utils.load_data import load_data

project_root = Path(__file__).parent.parent
wild_places_path = project_root / "data" / "wild.json"
npcs_path: Path = project_root / "data" / "npcs.json"


class WildPlace(BaseModel):
    """Represents a place in the wilderness."""

    wild_places_data: dict = load_data(wild_places_path)

    region: str
    trait: str
    landmark: str
    structure: str
    discoveries: str
    activities: str
    hazards: str

    def __str__(self):
        return f"""
                A {self.trait} {self.region} where you can find a {self.landmark} and a {self.structure}. 
                There you can discover a {self.discoveries}. 
                There something happen related to a {self.activities}.
                And beware the {self.hazards}.
                """


def create_wild_place(**kwargs):
    wild_places_data: dict = load_data(wild_places_path)

    region: str = choice(wild_places_data["wilderness_region"])
    trait: str = choice(wild_places_data["wilderness_region_traits"])
    landmark: Optional[str] = choice(wild_places_data["wilderness_landmarks"])
    structure: Optional[str] = choice(wild_places_data["wilderness_structures"])
    discoveries: Optional[str] = choice(wild_places_data["wilderness_discoveries"])
    activities: Optional[str] = choice(wild_places_data["wilderness_activities"])
    hazards: Optional[str] = choice(wild_places_data["wilderness_hazards"])

    # Overwrite defaults with provided keyword arguments
    data = {**locals(), **kwargs}  # Combine local variables and kwargs

    return WildPlace(**data)


def random_wilderness_npc():
    return create_npc(region="npc_wilderness")


if __name__ == "__main__":
    place = create_wild_place()
    print(place)
    print(" ")
    npc = random_wilderness_npc()
    print(npc)
