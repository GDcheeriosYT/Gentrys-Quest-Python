# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class JackSmidt(Character):
    def __init__(self):
        super().__init__(
            "Jack Smidt",
            "A dank wizard",
            StarRating(5),
            None,
            None,
            default_attack_points=2,
            default_defense_points=1,
            default_crit_rate_points=1
        )
