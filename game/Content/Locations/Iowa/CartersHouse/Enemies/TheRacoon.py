# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.RacoonPaws import RacoonPaws


class TheRacoon(Enemy):
    def __init__(self):
        super().__init__(
            "The Racoon that lives underneath my house",
            0,
            2,
            2,
            RacoonPaws(),
            "Uh Oh, his parents are angry at him again.",
            Experience()
        )
