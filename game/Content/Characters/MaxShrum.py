# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class MaxShrum(Character):
    def __init__(self):
        super().__init__(
            "Max Shrum",
            "Minecraft player thing",
            StarRating(4),
            None,
            None,
            default_health_points=2,
            default_attack_points=1
        )
