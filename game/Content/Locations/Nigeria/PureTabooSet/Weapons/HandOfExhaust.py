# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.StarRating import StarRating


class HandOfExhaust(Weapon):
    def __init__(self):
        super().__init__(
            "Hand of Exhaust",
            "A very used \"adult toy\"",
            "Adult Toy",
            0,
            star_rating=StarRating(5)
        )
