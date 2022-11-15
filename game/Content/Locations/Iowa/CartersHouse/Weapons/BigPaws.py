# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class BigPaws(Weapon):
    def __init__(self):
        super().__init__(
            "Big Paws",
            "Pair of big paws on a good boy!",
            "Paws",
            15,
            Buff(),
            Verbs("pounced on", "bit"),
            StarRating(3),
            Experience()
        )
