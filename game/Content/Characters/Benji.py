# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class Benji(Character):
    def __init__(self):
        super().__init__(
            "Benji",
            "He was born a very lucky boy.",
            StarRating(4),
            None,
            None,
            default_crit_rate_points=3
        )
