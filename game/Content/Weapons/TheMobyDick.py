# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class TheMobyDick(Weapon):
    def __init__(self):
        super().__init__(
            "The Moby Dick",
            "Toes? Na, it pulls hoes.",
            "Adult Toy",
            50,
            Buff(),
            Verbs("stuck", "inserted in"),
            StarRating(5)
        )
