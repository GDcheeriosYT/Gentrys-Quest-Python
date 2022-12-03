# game packages
# entity packages
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class Disc(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Disc",
            star_rating,
            "Mr.Gentry",
            Buff()
        )


class BeginnersGuideToPythonProgrammingTextbook(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Beginner's Guide to Python Programming Textbook",
            star_rating,
            "Mr.Gentry",
            Buff()
        )


class NecklaceMadeOfAlligatorTeeth(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Necklace Made of Alligator Teeth",
            star_rating,
            "Mr.Gentry",
            Buff()
        )


class SnowBoots(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Snow Boots",
            star_rating,
            "Mr.Gentry",
            Buff()
        )


class KaleSalad(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Kale Salad",
            star_rating,
            "Mr.Gentry",
            Buff()
        )
