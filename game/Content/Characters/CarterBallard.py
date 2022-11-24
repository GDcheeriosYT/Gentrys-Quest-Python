# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class CarterBallard(Character):
    def __init__(self):
        super().__init__(
            "Carter Ballard",
            "A regular guy with the physique of a Greek God!(also has very large biceps and is super cool).",
            StarRating(5),
            None,
            None,
            default_attack_points=4
        )
