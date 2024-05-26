from random import choice, randint
from typing import Optional

from pydantic import BaseModel

from src.the_wild import load_data as load_wild_data

places_data = load_wild_data()


class Place(BaseModel):
    """Represents a place in the wilderness."""

    region: str
    trait: str
    landmark: Optional[str] = None
    structure: Optional[str] = None
    discoveries: Optional[str] = None

    def __str__(self):
        return f"A {self.trait} {self.region} where you can find a {self.landmark} and a {self.structure}. There you can discover a {self.discoveries}."


def create_place():
    region: str = choice(places_data["wilderness_region"])
    trait: str = choice(places_data["wilderness_region_traits"])
    landmark: str = choice(places_data["wilderness_landmarks"])
    structure: str = choice(places_data["wilderness_structures"])
    discoveries: str = choice(places_data["wilderness_discoveries"])

    return Place(
        region=region,
        trait=trait,
        landmark=landmark,
        structure=structure,
        discoveries=discoveries,
    )


def hex_rouset():
    """A small region with 7 diferent locations

    Returns:
        _type_: _description_
    """
    places = []
    for i in range(7):
        place = create_place()
        places.append(place)
    return places


if __name__ == "__main__":
    h = hex_rouset()
    days = randint(3, 8)

    print(f"Vocês tem {days} dias para terminar a aventura.")
    for p in h:
        print("")
        print(p)
