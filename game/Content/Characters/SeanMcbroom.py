# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class SeanMcbroom(Character):
    def __init__(self):
        super().__init__(
            "Sean Mcbroom",
            "Fart nuts",
            StarRating(5),
            None,
            None,
            default_attack_points=2,
            default_defense_points=1,
            default_crit_damage_points=1
        )
