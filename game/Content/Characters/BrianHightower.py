# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class BrianHightower(Character):
    def __init__(self):
        super().__init__(
            "Brian Hightower",
            "description.",
            StarRating(5),
            None,
            None,
            default_attack_points=2,
            default_defense_points=2
        )
