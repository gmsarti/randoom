import random


def generate_character_stats():
    """Rolls 3d6 for each character stat, with an option for a reroll,
    and calculates the corresponding modifier."""

    stats = [
        "Strength",
        "Dexterity",
        "Constitution",
        "Intelligence",
        "Wisdom",
        "Charisma",
    ]
    results = {}
    modifiers = {
        1: -4,
        2: -4,
        3: -4,
        4: -3,
        5: -3,
        6: -2,
        7: -2,
        8: -1,
        9: -1,
        10: 0,
        11: 0,
        12: 1,
        13: 1,
        14: 2,
        15: 2,
        16: 3,
        17: 3,
        18: 4,
        19: 4,
        20: 4,
    }

    while True:
        for stat in stats:
            score = sum(random.randint(1, 6) for _ in range(3))
            results[stat] = score
            results[f"{stat} Modifier"] = modifiers[score]

        if any(score >= 14 for score in results.values()):
            break
        else:
            print("No stat is 14 or higher. Rolling again...")

    return results


if __name__ == "__main__":
    stats = generate_character_stats()
    for stat, score in stats.items():
        print(f"{stat}: {score}")
