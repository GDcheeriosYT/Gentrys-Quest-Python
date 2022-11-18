# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class MaxTramontina(Character):
    def __init__(self):
        super().__init__(
            "Max Tramontina",
            "description",
            StarRating(3),
            None,
            None,
            default_health_points=1,
            default_crit_rate_points=1
        )
