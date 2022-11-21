# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class SharpThrowingCards(Weapon):
    def __init__(self):
        super().__init__(
            "Sharp Throwing Cards",
            "Tactical throwing cards",
            "Playing Cards",
            33,
            Buff(StatTypes.CritRate),
            Verbs("grazed", "sliced"),
            StarRating(5)
        )
