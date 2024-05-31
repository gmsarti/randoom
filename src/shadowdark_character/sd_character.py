from random import choice, randint

from pydantic import BaseModel, Field


class Character(BaseModel):
    strength: int = Field(0, ge=0, le=20)
    dexterity: int = Field(0, ge=0, le=20)
    constitution: int = Field(0, ge=0, le=20)
    intelligence: int = Field(0, ge=0, le=20)
    wisdom: int = Field(0, ge=0, le=20)
    charisma: int = Field(0, ge=0, le=20)

    ancestry: str
    background: str

    character_class: str

    talents: str

    def __str__(self):
        return f"""
                A {self.character_class} {self.ancestry}.
                {self.background}.
                
                ATRIBUTES:
                STR: {self.strength}\tDEX: {self.dexterity}\tCONS :{self.constitution}
                INT: {self.intelligence}\tWIS: {self.wisdom}\tCHA :{self.charisma}
                
                TALENTS:
                {self.talents}
                """


def generate_stat():
    return sum([randint(1, 6) for _ in range(3)])


def get_class(strength, dexterity, constitution, intelligence, wisdom, charisma):
    character_classes = {
        "fighter": strength,
        "thief": dexterity,
        "wizard": intelligence,
        "priest": wisdom,
    }

    max_value = max(character_classes.values())
    probable_classes = [
        key for key, value in character_classes.items() if value == max_value
    ]
    character_class = choice(probable_classes)
    return character_class


def get_class_talent(character_class):
    basic_talents = {
        "fighter": [
            "Can use all weapons",
            "Can use all armor and shields",
            "Hauler. Add your Constitution modifier, if positive, to your gear slots.",
            "Grit. Choose Strength or Dexterity. You have advantage on checks of that type to overcome an opposing force, such as kicking open a stuck door (Strength) or slipping free of rusty chains (Dexterity)",
        ],
        "priest": [
            "Weapons: Club, crossbow, dagger, mace, longsword, staff, warhammer",
            "Armor: All armor and shields",
            "Languages. You know Celestial, Diabolic, or Primordial.",
            "Turn Undead. You know the turn undead spell. It doesn’t count toward your number of known spells.",
            "Deity. Choose a god to serve who matches your alignment (see Deities, pg. 28). You have a holy symbol for your god (it takes up no gear slots).",
            "Spellcasting. You can cast priest spells you know.",
        ],
        "thief": [
            "Weapons: Club, crossbow, dagger, shortbow, shortsword",
            "Armor: Leather armor, mithral chainmail",
            "Backstab. If you hit a creature who is unaware of your attack, you deal an extra weapon die of damage. Add additional weapon dice of damage equal to half your level (round down).",
            "Thievery. You are adept at thieving skills and have the necessary tools of the trade secreted on your person (they take up no gear slots). You are trained in the following tasks and have advantage on any associated checks: Climbing, Sneaking and hiding, Applying disguises, Finding and disabling traps Delicate tasks such as picking pockets and opening locks",
        ],
        "wizard": [
            "Weapons: Dagger, staff",
            "Armor: None",
            "Languages. You know two additional common languages and two rare languages (see pg. 32).",
            "Learning Spells. You can permanently learn a wizard spell from a spell scroll by studying it for a day and succeeding on a DC 15 Intelligence check. Whether you succeed or fail, you expend the spell scroll. Spells you learn in this way don't count toward your known spells.",
            "Spellcasting. You can castwizard spells you know.",
        ],
    }

    roll = sum([randint(1, 6) for _ in range(2)])

    random_talents = {
        "fighter": {
            2: "Gain Weapon Mastery with one additional weapon type",
            3: "+1 to melee and ranged attacks",
            4: "+1 to melee and ranged attacks",
            5: "+1 to melee and ranged attacks",
            6: "+1 to melee and ranged attacks",
            7: "+2 to Strength, Dexterity, or Constitution stat",
            8: "+2 to Strength, Dexterity, or Constitution stat",
            9: "+2 to Strength, Dexterity, or Constitution stat",
            10: "Choose one kind of armor. You get +1 AC from that armor",
            11: "Choose one kind of armor. You get +1 AC from that armor",
            12: "Choose a talent or +2 points to distribute to stats",
        },
        "priest": {
            2: "Gain advantage on casting one spell you know",
            3: "+1 to melee or ranged attacks",
            4: "+1 to melee or ranged attacks",
            5: "+1 to melee or ranged attacks",
            6: "+1 to melee or ranged attacks",
            7: "+1 to priest spellcasting checks",
            8: "+1 to priest spellcasting checks",
            9: "+1 to priest spellcasting checks",
            10: "+2 to Strength or Wisdom stat",
            11: "+2 to Strength or Wisdom stat",
            12: "Choose a talent or +2 points to distribute to stats",
        },
        "thief": {
            2: "Gain advantage on initiative rolls (reroll if duplicate)",
            3: "Backstab deals +1 dice of damage",
            4: "Backstab deals +1 dice of damage",
            5: "Backstab deals +1 dice of damage",
            6: "+2 to Strength, Dexterity, or Charisma stat",
            7: "+2 to Strength, Dexterity, or Charisma stat",
            8: "+2 to Strength, Dexterity, or Charisma stat",
            9: "+2 to Strength, Dexterity, or Charisma stat",
            10: "+1 to melee and ranged attacks",
            11: "+1 to melee and ranged attacks",
            12: "Choose a talent or +2 points to distribute to stats",
        },
        "wizard": {
            2: "Make 1 random magic item of a type you choose (pg. 282)",
            3: "+2 to Intelligence stat",
            4: "+2 to Intelligence stat",
            5: "+2 to Intelligence stat",
            6: "+2 to Intelligence stat",
            7: "+1 to wizard spellcasting checks",
            8: "Gain advantage on casting one spell you know",
            9: "Gain advantage on casting one spell you know",
            10: "Learn one additional wizard spell of any tier you know",
            11: "Learn one additional wizard spell of any tier you know",
            12: "Choose a talent or +2 points to distribute to stats",
        },
    }

    basic_talents[character_class].append(random_talents[character_class][roll])

    return basic_talents[character_class]


def get_ancestry():
    roll: int = randint(1, 12)
    ancestry = {
        1: "Human",
        2: "Human",
        3: "Human",
        4: "Human",
        5: "Elf",
        6: "Elf",
        7: "Dwarf",
        8: "Dwarf",
        9: "Dwarf",
        10: "Halfling",
        11: "Half-orc",
        12: "Goblin",
    }[roll]
    return ancestry


def get_background():
    """Rolls a d20 and returns the corresponding background."""

    roll = randint(1, 20)
    background = {
        1: "Urchin. You grew up in the merciless streets of a large city",
        2: "Wanted. There's a price on your head, but you have allies",
        3: "Cult Initiate. You know blasphemous secrets and rituals",
        4: "Thieves' Guild. You have connections, contacts, and debts",
        5: "Banished. Your people cast you out for supposed crimes",
        6: "Orphaned. An unusual guardian rescued and raised you",
        7: "Wizard's Apprentice. You have a knack and eye for magic",
        8: "Jeweler. You can easily appraise value and authenticity",
        9: "Herbalist. You know plants, medicines, and poisons",
        10: "Barbarian. You left the horde, but it never quite left you",
        11: "Mercenary. You fought friend and foe alike for your coin",
        12: "Sailor. Pirate, privateer, or merchant — the seas are yours",
        13: "Acolyte. You're well trained in religious rites and doctrines",
        14: "Soldier. You served as a fighter in an organized army",
        15: "Ranger. The woods and wilds are your true home",
        16: "Scout. You survived on stealth, observation, and speed",
        17: "Minstrel. You've traveled far with your charm and talent",
        18: "Scholar. You know much about ancient history and lore",
        19: "Noble. A famous name has opened many doors for you",
        20: "Chirurgeon. You know anatomy, surgery, and first aid",
    }[roll]
    return background


def generate_character(**kwargs):
    while True:
        strength = generate_stat()
        dexterity = generate_stat()
        constitution = generate_stat()
        intelligence = generate_stat()
        wisdom = generate_stat()
        charisma = generate_stat()

        stats = [strength, dexterity, constitution, intelligence, wisdom, charisma]

        if any(num > 13 for num in stats):
            break

    ancestry = get_ancestry()

    character_class = get_class(
        strength=strength,
        dexterity=dexterity,
        constitution=constitution,
        intelligence=intelligence,
        wisdom=wisdom,
        charisma=charisma,
    )

    background = get_background()

    talents = "\n".join(get_class_talent(character_class))

    data = {**locals(), **kwargs}

    return Character(**data)


if __name__ == "__main__":
    carlos = generate_character()
    print(carlos)
