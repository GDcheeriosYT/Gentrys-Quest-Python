# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.CustomerServicePhone import CustomerServicePhone


class CustomerServiceManager(Enemy):
    def __init__(self):
        super().__init__(
            "Customer Service Manager",
            1,
            1,
            2,
            CustomerServicePhone(),
            "Average Joe.",
            Experience()
        )
