# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class MasonJames(Character):
    def __init__(self):
        super().__init__(
            "Mason James",
            "description.",
            StarRating(5),
            None,
            None,
            default_attack_points=4
        )
