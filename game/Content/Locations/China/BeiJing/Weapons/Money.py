# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class Money(Weapon):
    def __init__(self):
        super().__init__(
            "Money",
            "Yi Long Ma (younger brother of Elon Musk) has more money than he does!",
            "sword",
            5,
            Buff(),
            Verbs("gave it to you", "slapped"),
            StarRating(5),
            Experience()
        )
