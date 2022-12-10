# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.RollingPin import RollingPin


class Baker(Enemy):
    def __init__(self):
        super().__init__(
            "Baker",
            2,
            1,
            2,
            RollingPin(),
            "Wow, this guy makes some mean bread. Not very nice though...",
            Experience()
        )
