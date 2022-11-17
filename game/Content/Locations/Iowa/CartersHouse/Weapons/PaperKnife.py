# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class PaperKnife(Weapon):
    def __init__(self):
        super().__init__(
            "Paper Knife",
            "A Paper Knife that is actually pretty sharp.",
            "Knife",
            8,
            Buff(),
            Verbs("pounced on", "bit"),
            StarRating(1),
            Experience()
        )
