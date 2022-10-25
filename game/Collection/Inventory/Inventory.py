# game packages
# collection packages
from .ArtifactList import ArtifactList
from .CharacterList import CharacterList
from .WeaponList import WeaponList

# graphics packages
from Graphics.Content.Text.WarningText import WarningText

# IO packages
from IO.Input import get_int


class Inventory:
    """
    Holds all the users owned items

    returns an Inventory

    parameters

    inventory_data: json object
        data used to construct inventory
    """

    inventory_data = None
    character_list = None
    artifact_list = None
    weapon_list = None
    money = None

    def __init__(self, inventory_data):
        self.money = inventory_data["money"]
        self.character_list = CharacterList(inventory_data["characters"])
        self.weapon_list = WeaponList(inventory_data["weapons"])
        self.artifact_list = ArtifactList(inventory_data["artifacts"])

    def upgrade(self):
        pass

    def manage_input(self):
        while True:
            try:
                num = get_int(self.__repr__())
                if num == 1:
                    self.character_list.list_characters()
                elif num == 2:
                    self.weapon_list.list_weapons()
                elif num == 3:
                    self.artifact_list.list_artifacts()
            except ValueError:
                WarningText("That's not exactly a number...")
            except IndexError:
                break

    def __repr__(self):
        return (
            f"""
${self.money}
1. characters {len(self.character_list.characters)}
2. weapons {len(self.weapon_list.weapons)}
3. artifacts {len(self.artifact_list.artifacts)}
4. back
"""
        )
