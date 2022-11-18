# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class DualSabers(Weapon):
    def __init__(self):
        super().__init__(
            "Dual Sabers",
            "The dual sabers, plucked from the depths of hell.",
            "Saber",
            32,
            Buff(StatTypes.CritDamage),
            Verbs("slashed", "mollywhopped"),
            StarRating(4)
        )
