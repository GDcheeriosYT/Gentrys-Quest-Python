# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.RacoonPaws import RacoonPaws


class RacoonInsideABackpack(Enemy):
    def __init__(self):
        super().__init__(
            "Racoon Inside of a Backpack",
            2,
            1,
            2,
            RacoonPaws(),
            "How did a racoon get inside of a backpack?",
            Experience()
        )
