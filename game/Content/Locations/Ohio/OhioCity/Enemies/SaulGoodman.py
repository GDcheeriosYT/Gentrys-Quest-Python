# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.Breifcase import Breifcase


class SaulGoodman(Enemy):
    def __init__(self):
        super().__init__(
            "Saul Goodman",
            3,
            1,
            1,
            Breifcase(),
            "Saul Goodman is the best lawyer you could ask for! As long as you pay him well...",
            Experience()
        )
