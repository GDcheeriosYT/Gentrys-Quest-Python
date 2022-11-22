# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class LinLaoShi(Character):
    def __init__(self):
        super().__init__(
            "Lin 老师",
            "totally 7 feet tall",
            StarRating(5),
            None,
            None,
            default_attack_points=4
        )
