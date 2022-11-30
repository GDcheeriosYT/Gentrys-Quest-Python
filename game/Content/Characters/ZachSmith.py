# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class ZachSmith(Character):
    def __init__(self):
        super().__init__(
            "Zach Smith",
            "Zach.",
            StarRating(5),
            default_health_points=1,
            default_defense_points=1,
            default_attack_points=1,
            default_crit_damage_points=1
        )
