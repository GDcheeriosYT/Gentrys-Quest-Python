# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class Paws(Weapon):
    def __init__(self):
        super().__init__(
            "Paws",
            "Pair of paws on a chinchilla.",
            "Paws",
            0,
            Buff(),
            Verbs("pounced on", "bit"),
            StarRating(2),
            Experience()
        )
