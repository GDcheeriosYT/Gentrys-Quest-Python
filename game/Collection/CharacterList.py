# game packages
# entity packages
from ..Entity.Character.Character import Character
from ..Entity.Stats.Experience import Experience
from ..Entity.Weapon.Weapon import Weapon
from ..Entity.Stats.Buff import Buff

# graphics packages
from ..Graphics.Content.Text.InfoText import InfoText


class CharacterList:
    """
    Makes a list of characters

    parameters:
    characters: list
        the list of characters
    """

    characters = None

    def __init__(self, characters=[]):
        self.characters = []
        counter = 0
        for character in characters:
            experience = character["experience"]
            equips = character["equips"]
            weapon = equips["weapon"]
            new_character = Character(
                character["name"],
                character["description"],
                character["star rating"],
                Experience(
                    experience["level"],
                    experience["xp"],
                    experience["xp required"]
                ),
                Weapon(
                    weapon["name"],
                    weapon["description"],
                    weapon["stats"]["attack"],
                    Buff(
                        weapon["stats"]
                    ),
                )
            )
            counter += 1
            InfoText(f"characters {counter/len(characters)}%").display()
