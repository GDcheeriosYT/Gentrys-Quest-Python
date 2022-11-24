# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class CharlieJohnson(Character):
    def __init__(self):
        super().__init__(
            "Charlie Johnson",
            "He used to be skinny, but he ate too much kfc.",
            StarRating(5),
            None,
            None,
            default_health_points=3,
            default_crit_rate_points=1
        )
