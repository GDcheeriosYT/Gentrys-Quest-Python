# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class Scanner(Weapon):
    def __init__(self):
        super().__init__(
            "Scanner",
            "That scanner people at the store always use.",
            "Club",
            0,
            Buff(),
            Verbs("scanned", "told an unrelatable story to"),
            StarRating(2),
            Experience()
        )
