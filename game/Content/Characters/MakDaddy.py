# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class MakDaddy(Character):
    def __init__(self):
        super().__init__(
            "Mak Daddy",
            "4 foot 11 and 40 pounds but big strong.",
            StarRating(5),
            None,
            None,
            default_health_points=1,
            default_attack_points=2,
            default_defense_points=1
        )
