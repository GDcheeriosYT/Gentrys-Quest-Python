# game packages
# entity packages
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class TrashCanLid(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Trash Can Lid",
            star_rating,
            "Down Town",
            Buff(StatTypes.Defense)
        )


class Suit(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Suit",
            star_rating,
            "Down Town",
            Buff(StatTypes.Defense)
        )


class Jacket(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Jacket",
            star_rating,
            "Down Town",
            Buff(StatTypes.Defense)
        )


class CarKeys(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Car Keys",
            star_rating,
            "Down Town",
            Buff()
        )


class CarboardBox(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Cardboard Box",
            star_rating,
            "Down Town",
            Buff()
        )


class MoldyCheese(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Moldy Cheese",
            star_rating,
            "Down Town",
            Buff()
        )


class EmptyBeerBottle(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Trash Can Lid",
            star_rating,
            "Down Town",
            Buff(StatTypes.Attack)
        )
