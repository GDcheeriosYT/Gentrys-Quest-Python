# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.Briefcase import Briefcase

class SaulGoodman(Enemy):
    def __init__(self):
        super().__init__(
            "Saul Goodman",
            3,
            1,
            1,
            Briefcase(),
            "Saul Goodman is the best lawyer you could ask for! As long as you pay him well...",
            Experience()
        )
