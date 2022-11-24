# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class NightStick(Weapon):
    def __init__(self):
        super().__init__(
            "Night Stick",
            "It sounds cool but really it is just a flashlight.",
            "club",
            0,
            Buff(),
            Verbs("beat", "bludgeoned"),
            StarRating(1),
            Experience()
        )
