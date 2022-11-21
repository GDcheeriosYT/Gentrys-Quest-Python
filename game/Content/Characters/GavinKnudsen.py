# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class GavinKnudsen(Character):
    def __init__(self):
        super().__init__(
            "Gavin Knudsen",
            "description",
            StarRating(2),
            None,
            None,
            default_attack_points=1
        )
