# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class HentaiMan(Character):
    def __init__(self):
        super().__init__(
            "Hentai Man",
            "Weaponized hentai.",
            StarRating(5),
            None,
            None,
            default_crit_rate_points=4
        )
