# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class CoolWeapon(Weapon):
    def __init__(self):
        super().__init__(
            "Cool Weapon",
            "Super cool sword.\nOnly the coolest of the cool wield this sword.",
            "Sword",
            43,
            Buff(StatTypes.Attack),
            Verbs("sweetified", "coolified"),
            StarRating(5)
        )
