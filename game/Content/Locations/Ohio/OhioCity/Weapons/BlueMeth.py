# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class BlueMeth(Weapon):
    def __init__(self):
        super().__init__(
            "Blue Meth",
            "The Blue Meth that Walter White has cooked(it has a 99% purity).",
            "Bad Medicine",
            0,
            Buff(),
            Verbs("threw", "farted on"),
            StarRating(3),
            Experience()
        )