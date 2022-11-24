# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class Clipboard(Weapon):
    def __init__(self):
        super().__init__(
            "Clipboard",
            "A clipboard held by an Osha Worker",
            "Clipboard",
            0,
            Buff(),
            Verbs("smacked", "broke the clipboard in the process of smacking"),
            StarRating(1),
            Experience()
        )
