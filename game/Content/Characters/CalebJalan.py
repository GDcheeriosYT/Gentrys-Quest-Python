# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class CalabJalan(Character):
    def __init__(self):
        super().__init__(
            "Caleb Jalan",
            "Dude I don't know.",
            StarRating(3),
            None,
            None,
            default_health_points=1,
            default_crit_damage_points=1
        )
