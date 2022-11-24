# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class JayceeMaiers(Character):
    def __init__(self):
        super().__init__(
            "Jaycee Maiers",
            "The booty builder.",
            StarRating(5),
            None,
            None,
            default_health_points=2,
            default_attack_points=1,
            default_defense_points=1
        )
