# game packages
# entity packages
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes

class ManscappedRazorBundle(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Manscapped Razor Bundle",
            star_rating,
            "Nolan Anderson",
            Buff(StatTypes.Attack)
        )

class Lubricant(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Lubricant",
            star_rating,
            "Nolan Anderson",
            Buff(StatTypes.Defense)
        )

class PondWater(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Pond Water",
            star_rating,
            "Nolan Anderson",
            Buff(StatTypes.Health)
        )

class ChikFilABurrito(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Chik-Fil-A Burrito",
            star_rating,
            "Nolan Anderson",
            Buff(StatTypes.Defense)
        )

class SpicyStick(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Spicy Stick",
            star_rating,
            "Nolan Anderson",
            Buff(StatTypes.Attack)
        )