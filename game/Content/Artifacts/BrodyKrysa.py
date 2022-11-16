# game packages
# entity packages
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes

class ChalkBag(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Chalk Bag",
            star_rating,
            "Brody Krysa",
            Buff(StatTypes.CritRate)
        )

class ClimbingShoes(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Climbing Shoes",
            star_rating,
            "Brody Krysa",
            Buff(StatTypes.CritRate)
        )

class Harness(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Harness",
            star_rating,
            "Brody Krysa",
            Buff(StatTypes.CritRate)
        )

class BelayDevice(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Belay Device",
            star_rating,
            "Brody Krysa",
            Buff(StatTypes.CritRate)
        )

class Karabiner(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Karabiner",
            star_rating,
            "Brody Krysa",
            Buff(StatTypes.CritRate)
        )