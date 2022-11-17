from enum import Enum


class StatTypes(Enum):
    Health = 1
    Attack = 2
    Defense = 3
    CritRate = 4
    CritDamage = 5
    #Strength = 5
    #Magic = 6
    #Magic_Defense = 7
    #Arcane = 8
    #Dexterity = 9
    
    def __repr__(self):
        return self.name
