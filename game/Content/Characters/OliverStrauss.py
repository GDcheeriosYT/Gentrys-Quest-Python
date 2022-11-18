# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class OliverStrauss(Character):
    def __init__(self):
        super().__init__(
            "Oliver Strauss",
            "Sneaky boi, has many females.",
            StarRating(5),
            None,
            None,
            default_crit_rate_points=2,
            default_crit_damage_points=2
        )
