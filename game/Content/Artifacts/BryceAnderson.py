# game packages
# entity packages
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class MurphysNuts(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Murphy's Nuts",
            star_rating,
            "Bryce Anderson",
            Buff(StatTypes.Health)
        )

class QuandaleDingleFartInAJar(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Quandale Dingle Fart In A Jar",
            star_rating,
            "Bryce Anderson",
            Buff(StatTypes.Attack)
        )

class ButtahDog(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Buttah Dog",
            star_rating,
            "Bryce Anderson",
            Buff(StatTypes.Defense)
        )

class NyanCat(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Nyan Cat",
            star_rating,
            "Bryce Anderson",
            Buff(StatTypes.CritRate)
        )

class AngryAnubis(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Angry Anubis",
            star_rating,
            "Bryce Anderson",
            Buff(StatTypes.CritRate)
        )