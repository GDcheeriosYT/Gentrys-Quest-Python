# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class TeslaStock(Weapon):
    def __init__(self):
        super().__init__(
            "Tesla Stock",
            "Tesla Stock (although it has dropped) is still fantastic as a stock... It's also a great weapon!",
            "Stock",
            5,
            Buff(),
            Verbs("invested in", "bought up"),
            StarRating(5),
            Experience()
        )