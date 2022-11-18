# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class KchuntMan(Character):
    def __init__(self):
        super().__init__(
            "KchuntMan",
            "Stealth Mode.",
            StarRating(5),
            None,
            None,
            default_crit_rate_points=4
        )
