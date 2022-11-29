# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class MJ(Character):
    def __init__(self):
        super().__init__(
            "MJ",
            "Totally taller than lin老师",
            StarRating(5),
            default_attack_points=4
        )