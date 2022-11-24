# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class Masonator(Weapon):
    def __init__(self):
        super().__init__(
            "Masonator",
            "THE TOOTHBRUSH.\nThis toothbrush has been handed down for generations upon generations by the greek gods. You must be worthy of the brush to obtain this brush.",
            "Toothbrush",
            34,
            Buff(StatTypes.CritDamage),
            Verbs("brushed", "squirted toothpaste on"),
            StarRating(5)
        )
