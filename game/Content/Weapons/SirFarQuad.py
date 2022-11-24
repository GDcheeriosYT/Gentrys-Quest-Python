# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class SirFarQuad(Weapon):
    def __init__(self):
        super().__init__(
            "Sir Far Quad",
            "Long long sword.",
            "Lance",
            50,
            Buff(StatTypes.CritDamage),
            Verbs("impaled", "sliced"),
            StarRating(5)
        )
