# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class LittleMuscles(Weapon):
    def __init__(self):
        super().__init__(
            "Little Muscles",
            "Looks can be deceiving",
            "Muscle",
            1,
            Buff(),
            Verbs("punches up at", "flashed the project of"),
            StarRating(2)
        )
