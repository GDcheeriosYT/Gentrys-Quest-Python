# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class ImpostersKnife(Weapon):
    def __init__(self):
        super().__init__(
            "Imposter's Knife",
            "The imposters knife is extremely deadly... especially if you are a crewmate.",
            "Knife",
            0,
            Buff(),
            Verbs("sliced *imposter noises play*", "cut *imposter noises play*"),
            StarRating(4),
            Experience()
        )
