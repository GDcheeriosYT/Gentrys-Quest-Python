# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.Briefcase import Briefcase


class BuisinessMan(Enemy):
    def __init__(self):
        super().__init__(
            "Buisiness Man",
            2,
            2,
            0,
            Briefcase(),
            Experience()
        )
