from pathlib import Path
from random import choice
from typing import Optional

from pydantic import BaseModel
from utils.load_data import load_data

project_root = Path(__file__).parent.parent
wild_places_path = project_root / "data" / "wild.json"
npcs_path: Path = project_root / "data" / "npcs.json"


class WildPlace(BaseModel):
    """Represents a place in the wilderness."""

    wild_places_data: dict = load_data(wild_places_path)

    region: str = choice(wild_places_data["wilderness_region"])
    trait: str = choice(wild_places_data["wilderness_region_traits"])
    landmark: Optional[str] = choice(wild_places_data["wilderness_landmarks"])
    structure: Optional[str] = choice(wild_places_data["wilderness_structures"])
    discoveries: Optional[str] = choice(wild_places_data["wilderness_discoveries"])
    activities: Optional[str] = choice(wild_places_data["wilderness_activities"])
    hazards: Optional[str] = choice(wild_places_data["wilderness_hazards"])

    def __str__(self):
        return f"""
                A {self.trait} {self.region} where you can find a {self.landmark} and a {self.structure}. 
                There you can discover a {self.discoveries}. 
                There something happen related to a {self.activities}.
                And beware the {self.hazards}.
                """


class WildNPC(BaseModel):
    """Represents a person in the wilderness."""

    sex: str
    age: str
    job: str
    goal: str
    asset: str
    mission: str
    misfortune: str
    liability: str

    def __str__(self):
        return f"""
                A {self.age} {self.sex}  {self.job} with the asset: {self.asset}.
                Has the goal of {self.goal} and offer a mission related to {self.mission}.
                Has the missfortune {self.misfortune} and the liability {self.liability}
                """


def create_npc():
    wild_npc_data: dict = load_data(npcs_path)

    sex = choice(wild_npc_data["npc_sex"])
    age = choice(wild_npc_data["npc_age"])
    job = choice(wild_npc_data["npc_wilderness"])
    goal = choice(wild_npc_data["npc_goals"])
    asset = choice(wild_npc_data["npc_assets"])
    mission = choice(wild_npc_data["npc_misfortunes"])
    misfortune = choice(wild_npc_data["npc_missions"])
    liability = choice(wild_npc_data["npc_liabilities"])

    return WildNPC(
        sex=sex,
        age=age,
        job=job,
        goal=goal,
        asset=asset,
        mission=mission,
        misfortune=misfortune,
        liability=liability,
    )


def generate_npc(random_seed=None):
    return WildNPC(random_seed=random_seed)


if __name__ == "__main__":
    place = WildPlace()
    print(f"Place:\n{place}\n")
    print("PEOPLE OF INTEREST:")
    for i in range(4):
        new_npc = create_npc()
        print(f"PERSON {i}:\n{new_npc}\n")
