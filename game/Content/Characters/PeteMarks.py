# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class PeteMarks(Character):
    def __init__(self):
        super().__init__(
            "Pete Marks",
            "Can type really fast, but has zero b****s.",
            StarRating(4),
            default_crit_rate_points=3
        )