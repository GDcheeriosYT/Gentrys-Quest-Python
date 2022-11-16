# game packages
# entity packages
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class MacBook(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Mac Book",
            star_rating,
            "Alec Ferchen",
            Buff(StatTypes.CritDamage)
        )

class CanesTendies(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Canes Tendies",
            star_rating,
            "Alec Ferchen",
            Buff(StatTypes.Health)
        )

class Dog(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Dog",
            star_rating,
            "Alec Ferchen",
            Buff(StatTypes.Defense)
        )