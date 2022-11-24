# game packages
# entity packages
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class HyveeFuelSaverCard(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Hy-vee Fuel Saver Card",
            star_rating,
            "Hyvee",
            Buff()
        )


class HyveeBrandWater(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Hy-vee Brand Water",
            star_rating,
            "Hyvee",
            Buff()
        )


class HyveeBrandSpaghetti(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Hy-vee Brand Spaghetti",
            star_rating,
            "Hyvee",
            Buff()
        )


class HyveeBrandCandy(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Hy-vee Brand Candy",
            star_rating,
            "Hyvee",
            Buff()
        )


class HyveeBrandFruit(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Hy-vee Brand Fruit",
            star_rating,
            "Hyvee",
            Buff()
        )


class HyveeBrandCereal(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Hy-vee Brand Cereal",
            star_rating,
            "Hyvee",
            Buff()
        )


class LostCreditCard(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Lost Credit Card",
            star_rating,
            "Hyvee",
            Buff()
        )


class LostID(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Lost ID",
            star_rating,
            "Hyvee",
            Buff()
        )


class HyveeChinese(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Hy-vee Chinese",
            star_rating,
            "Hyvee",
            Buff()
        )
