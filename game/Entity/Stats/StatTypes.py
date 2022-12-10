from enum import Enum


class StatTypes(Enum):
    Health = 1
    Attack = 2
    Defense = 3
    CritRate = 4
    CritDamage = 5
    
    def __repr__(self):
        return self.name
