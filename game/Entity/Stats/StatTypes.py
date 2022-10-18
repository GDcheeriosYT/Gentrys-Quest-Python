from enum import Enum


class StatTypes(Enum):
    Health = 0
    Attack = 1
    Defense = 2
    CritRate = 3
    CritDamage = 4
    Strength = 5
    Magic = 6
    Magic_Defense = 7
    Arcane = 8
    Dexterity = 9
    
    def __repr__(self):
        return self.name
