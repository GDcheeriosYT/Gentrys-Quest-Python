# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class FireBreath(Weapon):
    def __init__(self):
        super().__init__(
            "Fire Breath",
            "The power of the Baby Dragon is to breathe fire.",
            "Breath",
            0,
            Buff(),
            Verbs("spewed flames", "spit flames"),
            StarRating(4),
            Experience()
        )