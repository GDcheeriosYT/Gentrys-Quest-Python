# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.FinsAndFlippers import FinsAndFlippers


class FishNamedBryan(Enemy):
    def __init__(self):
        super().__init__(
            "Fish Named Bryan",
            3,
            3,
            3,
            FinsAndFlippers(),
            "This fish's name happens to be Bryan:).",
            Experience()
        )
