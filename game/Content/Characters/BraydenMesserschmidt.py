# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class BraydenMesserschmidt(Character):
    def __init__(self):
        super().__init__(
            "Brayden Messerschmidt",
            "An osu player who formed a contract with ppy(Dean Herbert) to not talk to females.",
            StarRating(5),
            None,
            None,
            default_crit_rate_points=4
        )
