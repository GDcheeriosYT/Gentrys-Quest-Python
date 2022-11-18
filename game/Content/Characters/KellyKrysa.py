# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class KellyKrysa(Character):
    def __init__(self):
        super().__init__(
            "Kelly Krysa",
            "Apex Predator.",
            StarRating(4),
            None,
            None,
            default_health_points=1,
            default_attack_points=1,
            default_defense_points=1
        )
