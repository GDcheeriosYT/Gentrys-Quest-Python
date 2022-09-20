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
    characters = None
    artifacts = None
    weapons = None
    money = None

    def __init__(self, inventory_data):
        money = inventory_data["money"]
        characters = CharacterList(inventory_data["characters"])
        weapons = WeaponList(inventory_data["weapons"])
        artifacts = ArtifactList(inventory_data["artifacts"])
