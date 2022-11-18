# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Buff import Buff


class Hammer(Weapon):
    def __init__(self):
        super().__init__(
            "Hammer",
            "Just a hammer.",
            "Hammer",
            8,
            Buff(),
            Verbs("smashed", "slammed"),
            StarRating(1)
        )