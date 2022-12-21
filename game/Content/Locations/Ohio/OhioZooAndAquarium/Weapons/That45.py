# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class That45(Weapon):
    def __init__(self):
        super().__init__(
            "That .45",
            "The classic .45.",
            "Gun",
            0,
            Buff(),
            Verbs("shot", "pistol whipped"),
            StarRating(5),
            Experience()
        )