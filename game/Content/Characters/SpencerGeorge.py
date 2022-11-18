# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class SpencerGeorge(Character):
    def __init__(self):
        super().__init__(
            "Spizzle",
            "Gambling glass cannon.",
            StarRating(5),
            None,
            None,
            default_crit_rate_points=1,
            default_crit_damage_points=3
        )
