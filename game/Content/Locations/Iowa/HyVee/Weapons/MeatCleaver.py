# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class MeatCleaver(Weapon):
    def __init__(self):
        super().__init__(
            "Meat Cleaver",
            "The Meat Cleaver is a dangerous weapon... especially used against meat.",
            "Knife",
            2,
            Buff(),
            Verbs("cleaved", "cut"),
            StarRating(4),
            Experience()
        )
