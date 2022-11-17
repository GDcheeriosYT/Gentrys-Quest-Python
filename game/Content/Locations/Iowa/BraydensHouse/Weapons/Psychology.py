# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class Psychology(Weapon):
    def __init__(self):
        super().__init__(
            "Psychology",
            "A psychic weapon",
            "mental",
            0,
            Buff(),
            Verbs("messed with", "tricked"),
            StarRating(2),
            Experience()
        )
