from pathlib import Path
from random import choice, choices
from typing import Optional

from pydantic import BaseModel
from utils.load_data import load_data

project_root = Path(__file__).parent.parent
npcs_path: Path = project_root / "data" / "npcs.json"


class NonPlayableCharacter(BaseModel):
    """Represents a person in the wilderness."""

    sex: str
    age: str
    region: Optional[str]
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


def create_npc(**kwargs):  # Use **kwargs to capture all keyword arguments
    wild_npc_data: dict = load_data(npcs_path)

    # Default values from data
    sex = choices(wild_npc_data["npc_sex"], weights=[43, 43, 14], k=1)[0]
    age = choices(wild_npc_data["npc_age"], weights=[20, 55, 25], k=1)[0]
    region = choice(["npc_civilized", "npc_underworld", "npc_wilderness"])
    job = choice(wild_npc_data[region])
    goal = choice(wild_npc_data["npc_goals"])
    asset = choice(wild_npc_data["npc_assets"])
    mission = choice(wild_npc_data["npc_misfortunes"])
    misfortune = choice(wild_npc_data["npc_missions"])
    liability = choice(wild_npc_data["npc_liabilities"])

    # Overwrite defaults with provided keyword arguments
    data = {**locals(), **kwargs}  # Combine local variables and kwargs

    # Ensure job is consistent with region if region is overwritten
    if "region" in kwargs:
        data["job"] = choice(wild_npc_data[kwargs["region"]])

    return NonPlayableCharacter(**data)  # Pass the combined data to create the NPC


if __name__ == "__main__":
    npc1 = create_npc()  # Random NPC
    npc2 = create_npc(sex="female", region="npc_underworld")
    print(f"\nNPC1:\n{npc1}\nNPC2:\n{npc2}")
