# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class Pan(Weapon):
    def __init__(self):
        super().__init__(
            "Pan",
            "This pan is covered in grease. Gross.",
            "Club",
            0,
            Buff(),
            Verbs("whacked", "beat"),
            StarRating(2),
            Experience()
        )
