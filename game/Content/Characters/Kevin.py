# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class Kevin(Character):
    def __init__(self):
        super().__init__(
            "Kevin",
            "description.",
            StarRating(5),
            None,
            None,
            default_crit_damage_points=4
        )
