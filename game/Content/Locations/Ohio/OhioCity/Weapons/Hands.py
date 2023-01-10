# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class Hands(Weapon):
    def __init__(self):
        super().__init__(
            "Hands",
            "Pair of grubby hands used to fit inside of a spacesuit.",
            "Hands",
            0,
            Buff(),
            Verbs("poked", "hit"),
            StarRating(1),
            Experience()
        )