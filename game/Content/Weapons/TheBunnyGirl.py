# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class TheBunnyGirl(Weapon):
    def __init__(self):
        super().__init__(
            "The Bunny Girl",
            "Born from the highest luxurious bunny girl outfit fabric. A lustful weapon",
            "Katana",
            46,
            Buff(StatTypes.CritDamage),
            Verbs("tickled", "came inside"),
            StarRating(5)
        )
