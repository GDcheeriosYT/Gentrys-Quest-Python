# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.Zebra import Zebra


class TargetEmployee(Enemy):
    def __init__(self):
        weapon = Zebra()
        weapon.verbs.critical = "called over a manger to deal with"
        super().__init__(
            "Target Employee",
            0,
            1,
            0,
            weapon,
            "An employee",
            Experience()
        )
