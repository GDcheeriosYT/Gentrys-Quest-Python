from .ArtifactList import ArtifactList
from .CharacterList import CharacterList
from .WeaponList import WeaponList


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

    def __repr__(self):
        return (
            f"""
${self.money}
1. characters {len(self.character_list.characters)}
2. weapons {len(self.weapon_list.weapons)}
3. artifacts {len(self.artifact_list.artifacts)}
"""
        )
