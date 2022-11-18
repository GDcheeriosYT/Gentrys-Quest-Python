# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class JackBorland(Character):
    def __init__(self):
        super().__init__(
            "Jack Borland",
            "The chicken wiener collector.",
            StarRating(5),
            None,
            None,
            default_health_points=2,
            default_defense_points=1,
            default_crit_damage_points=1
        )
