# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs

# collection packages
from ..Handlers.BuffArrayHandler import BuffArrayHandler
from ..Handlers.ExperienceObjectHandler import ExperienceObjectHandler

# graphics packages
from Graphics.Status import Status

# built-in packages
import time

class WeaponList:
    """
    Makes a list of weapons

    parameters:
    weapons: list
        the list of weapons
    """

    weapons = None

    def __init__(self, weapons=[]):
        load_data_status = Status("Loading your weapon data", "dots")
        load_data_status.start()
        self.weapons = []
        for weapon in weapons:
            experience = weapon["experience"]
            stats = weapon["stats"]
            verbs = weapon["verbs"]
            verbs = Verbs(verbs["normal"], verbs["critical"])
            new_weapon = Weapon(
                weapon["name"],
                weapon["description"],
                weapon["weapon type"],
                weapon["stats"]["attack"],
                BuffArrayHandler(weapon["stats"]["buff"]).create_buff(),
                Verbs(weapon["verbs"]["normal"], weapon["verbs"]["critical"]),
                weapon["star rating"],
                ExperienceObjectHandler(weapon["experience"]).create_experience()
            )
            self.weapons.append(new_weapon)
            #time.sleep(0.1)
        load_data_status.stop()
