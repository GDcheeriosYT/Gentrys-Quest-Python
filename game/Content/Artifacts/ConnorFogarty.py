# game packages
# entity packages
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class Bone(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Bone",
            star_rating,
            "Connor Fogarty",
            Buff(StatTypes.Health)
        )

class MultiPetPigDogToy(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Multipet Pig Dog ToyⓇ",
            star_rating,
            "Connor Fogarty",
            Buff(StatTypes.CritRate)
        )

class CheeseWheel(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Cheese Wheel",
            star_rating,
            "Connor Fogarty",
            Buff(StatTypes.Defense)
        )

class SilkDogBed(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Silk Dog Toy",
            star_rating,
            "Connor Fogarty",
            Buff(StatTypes.CritDamage)
        )

class BellyRubMachine(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Belly Rub Machine",
            star_rating,
            "Connor Fogarty",
            Buff(StatTypes.Attack)
        )
