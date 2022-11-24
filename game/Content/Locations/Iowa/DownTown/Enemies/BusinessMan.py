# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.Briefcase import Briefcase


class BusinessMan(Enemy):
    def __init__(self):
        super().__init__(
            "Business Man",
            2,
            2,
            0,
            Briefcase(),
            "Just a business man",
            Experience()
        )
