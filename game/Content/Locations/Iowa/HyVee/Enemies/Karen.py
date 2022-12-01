# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.IPhone import IPhone


class Karen(Enemy):
    def __init__(self):
        super().__init__(
            "Karen",
            1,
            3,
            0,
            IPhone(),
            "Good ol' HyVee checkout guy... or girl I guess.",
            Experience()
        )
