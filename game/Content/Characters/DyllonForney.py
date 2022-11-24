# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class DyllonForney(Character):
    def __init__(self):
        super().__init__(
            "Dyllon Forney",
            "description",
            StarRating(3),
            None,
            None,
            default_attack_points=2
        )
