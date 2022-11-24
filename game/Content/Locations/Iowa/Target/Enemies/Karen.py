# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.Camera import Camera


class Karen(Enemy):
    def __init__(self):
        super().__init__(
            "Karen",
            1,
            1,
            1,
            Camera(),
            "A for some reason very angry woman.",
            Experience()
        )
