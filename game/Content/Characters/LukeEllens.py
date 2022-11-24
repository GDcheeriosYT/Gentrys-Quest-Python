# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class LukeEllens(Character):
    def __init__(self):
        super().__init__(
            "Luke Ellens",
            "Very F***ing athletic. Literally unstoppable in any athletic activity. Strategic god!",
            StarRating(5),
            default_health_points=1,
            default_defense_points=2,
            default_attack_points=1
        )
