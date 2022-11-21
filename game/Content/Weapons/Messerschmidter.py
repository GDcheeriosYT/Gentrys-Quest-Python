# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class Messerschmidter(Weapon):
    def __init__(self):
        super().__init__(
            "The Messerschmidter",
            "A life size version of Brayden Messerschmidt but as a sword.",
            "Sword",
            40,
            Buff(StatTypes.Attack),
            Verbs("with his messerschmidter tapped", "with his messerschmidter spat on"),
            StarRating(5)
        )
