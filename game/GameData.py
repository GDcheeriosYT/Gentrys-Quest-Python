# built-in packages
import json

# game packages
from Collection.Inventory.Inventory import Inventory

class GameData:
    """
    returns a GameData object with the given json string

    parameters

    json_string: string
        the game data json string
    """

    inventory = None
    startup_amount = None
    settings = None

    def __init__(self, json_data):
        if json_data == None:
            data = {
                "startupamount": 1,
                "settings": {},
                "inventory": {
                    "characters": [],
                    "artifacts": [],
                    "weapons": [],
                    "money": 0
                }
            }
            self.inventory = Inventory(data["inventory"])
            self.startup_amount = data["startupamount"]
            self.settings = data["settings"]
        else:
            json_object = json_data
            self.inventory = Inventory(json_object["inventory"])
            self.startup_amount = json_object["startupamount"]
            self.settings = json_object["settings"]

    def obtain(self):
        return self.inventory, self.startup_amount, self.settings
