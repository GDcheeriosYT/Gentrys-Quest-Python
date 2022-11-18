# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class ConnorMoya(Character):
    def __init__(self):
        super().__init__(
            "Connor Moya",
            "description",
            StarRating(2),
            None,
            None,
            default_crit_rate_points=1
        )
