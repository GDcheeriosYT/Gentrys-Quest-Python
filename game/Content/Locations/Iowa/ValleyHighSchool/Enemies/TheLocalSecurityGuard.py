# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.NightStick import NightStick


class TheLocalSecurityGuard(Enemy):
    def __init__(self):
        super().__init__(
            "The Local Security Guard",
            1,
            2,
            1,
            NightStick(),
            "I thought he was friendly:(.",
            Experience()
        )