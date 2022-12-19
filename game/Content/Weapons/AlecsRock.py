# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class AlecsRock(Weapon):
    def __init__(self):
        super().__init__(
            "Alec's Rock",
            "A small rock.",
            "Stone",
            28,
            Buff(StatTypes.Attack),
            Verbs("hit", "immensely bashed"),
            StarRating(2)
        )
