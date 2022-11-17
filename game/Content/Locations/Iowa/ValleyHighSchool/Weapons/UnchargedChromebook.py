# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class UnchargedChromebook(Weapon):
    def __init__(self):
        super().__init__(
            "Uncharged Chromebook",
            "Just a uncharged Chromebook.",
            "Sword",
            0,
            Buff(),
            Verbs("slapped", "hit"),
            StarRating(2),
            Experience()
        )
