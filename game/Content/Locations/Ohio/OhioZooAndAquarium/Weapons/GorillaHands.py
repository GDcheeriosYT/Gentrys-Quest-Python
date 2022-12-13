# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class GorillaHands(Weapon):
    def __init__(self):
        super().__init__(
            "Gorilla Hands",
            "Pair of BIG hands from a gorilla (From Ohio).",
            "Hands",
            0,
            Buff(),
            Verbs("beat", "bonked"),
            StarRating(3),
            Experience()
        )