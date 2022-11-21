# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class NathanTenney(Character):
    def __init__(self):
        super().__init__(
            "Nathan Tenney",
            "description.",
            StarRating(5),
            None,
            None,
            default_health_points=1,
            default_attack_points=1,
            default_defense_points=2
        )
