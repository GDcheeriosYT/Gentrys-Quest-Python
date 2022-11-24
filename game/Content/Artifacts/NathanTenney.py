# game packages
# entity packages
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class RubiksCube(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Rubik's Cube",
            star_rating,
            "Nathan Tenney",
            Buff(StatTypes.CritRate)
        )


class Fork(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Fork",
            star_rating,
            "Nathan Tenney",
            Buff(StatTypes.Attack)
        )


class Bucket(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Bucket",
            star_rating,
            "Nathan Tenney",
            Buff(StatTypes.Defense)
        )


class Globe(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Globe",
            star_rating,
            "Nathan Tenney",
            Buff(StatTypes.CritDamage)
        )


class Blanket(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Blanket",
            star_rating,
            "Nathan Tenney",
            Buff(StatTypes.Defense)
        )
