# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class LucasSmidt(Character):
    def __init__(self):
        super().__init__(
            "Lucas Smidt",
            "Totally rad guy who is super awesome.",
            StarRating(5),
            None,
            None,
            default_health_points=1,
            default_attack_points=2,
            default_defense_points=1
        )
