# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.That45 import That45


class RacoonWith45(Enemy):
    def __init__(self):
        super().__init__(
            "Racoon with the .45",
            1,
            3,
            1,
            That45(),
            "Winton Overwat...........",
            Experience()
        )
