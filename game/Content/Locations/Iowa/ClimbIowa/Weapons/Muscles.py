# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class Muscles(Weapon):
    def __init__(self):
        super().__init__(
            "Muscles",
            "Some nice looking muscles",
            "Muscle",
            1,
            Buff(),
            Verbs("confidently flexed on", "power screamed at"),
            StarRating(2)
        )
