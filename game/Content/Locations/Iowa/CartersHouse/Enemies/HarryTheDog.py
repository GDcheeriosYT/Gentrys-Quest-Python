# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.BigPaws import BigPaws


class HarryTheDog(Enemy):
    def __init__(self):
        super().__init__(
            "Harry The Dog",
            0,
            1,
            0,
            BigPaws(),
            "Harry the dog is quite a good boy.",
            Experience()
        )
