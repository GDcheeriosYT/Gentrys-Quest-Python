# built-in packages
import json

# game packages
from Collection import Inventory


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

    def __init__(self, json_string):
        if len(json_string) < 10:
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
            self.inventory = Inventory.Inventory(data["inventory"])
            self.startup_amount = data["startupamount"]
            self.settings = data["settings"]
        else:
            json_object = json.loads(json_string)
            self.inventory = Inventory.Inventory(json_object["inventory"])
            self.startup_amount = json_object["startupamount"]
            self.settings = json_object["settings"]
