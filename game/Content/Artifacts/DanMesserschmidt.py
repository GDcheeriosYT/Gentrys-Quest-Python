# game packages
# entity packages
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes

class Budweiser(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Budweiser",
            star_rating,
            "Dan Messerschmidt",
            Buff(StatTypes.Attack)
        )

class Tissues(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Tissues",
            star_rating,
            "Dan Messerschmidt",
            Buff(StatTypes.Defense)
        )

class BrokenKeyboard(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Broken Keyboard",
            star_rating,
            "Dan Messerschmidt",
            Buff(StatTypes.Defense)
        )

class Poop(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Poop",
            star_rating,
            "Dan Messerschmidt",
            Buff(StatTypes.Defense)
        )

class Nachos(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Nachos",
            star_rating,
            "Dan Messerschmidt",
            Buff(StatTypes.Defense)
        )
