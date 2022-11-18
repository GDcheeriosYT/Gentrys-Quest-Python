# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class DerekCorona(Character):
    def __init__(self):
        super().__init__(
            "Derek Corona",
            "A mexican assassin who can't keep away from alcohol.",
            StarRating(5),
            None,
            None,
            default_health_points=2,
            default_attack_points=1,
            default_crit_damage_points=1
        )
