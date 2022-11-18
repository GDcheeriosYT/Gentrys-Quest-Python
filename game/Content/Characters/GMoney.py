# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class GMoney(Character):
    def __init__(self):
        super().__init__(
            "Gmoney(Mr.Gentry)",
            "Hyplains Drifter.",
            StarRating(5),
            None,
            None,
            default_health_points=2,
            default_attack_points=2
        )
