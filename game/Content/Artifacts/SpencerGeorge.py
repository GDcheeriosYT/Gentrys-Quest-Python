# game packages
# entity packages
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class AceUpTheSleeve(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Ace Up The Sleeve",
            star_rating,
            "Spencer George",
            Buff(StatTypes.CritDamage)
        )

class HalfEatenSandwich(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Half Eaten Sandwich",
            star_rating,
            "Spencer George",
            Buff(StatTypes.Health)
        )

class WeightedDice(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Weighted Dice",
            star_rating,
            "Spencer George",
            Buff(StatTypes.Defense)
        )

class RouletteWheel(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Roulette Wheel",
            star_rating,
            "Spencer George",
            Buff(StatTypes.Attack)
        )

class Bouncer(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Bouncer",
            star_rating,
            "Spencer George",
            Buff(StatTypes.Defense)
        )