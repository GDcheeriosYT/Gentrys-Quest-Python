# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class HannaHardy(Character):
    def __init__(self):
        super().__init__(
            "Hanna Hardy",
            "IDK",
            StarRating(4),
            None,
            None,
            default_health_points=1,
            default_attack_points=1,
            default_crit_rate_points=1
        )
