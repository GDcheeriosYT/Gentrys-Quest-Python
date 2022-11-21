# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class AsherLane(Character):
    def __init__(self):
        super().__init__(
            "Asher Lane",
            "Pray to the goddess honey.",
            StarRating(3),
            None,
            None,
            default_attack_points=1,
            default_crit_rate_points=1
        )
