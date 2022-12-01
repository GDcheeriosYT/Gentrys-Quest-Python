# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class CustomerServicePhone(Weapon):
    def __init__(self):
        super().__init__(
            "Customer Service Phone",
            "The Customer Service Phone is a sacred weapon... Not really though.",
            "Club",
            0,
            Buff(),
            Verbs("bludgeoned", "beat"),
            StarRating(1),
            Experience()
        )
