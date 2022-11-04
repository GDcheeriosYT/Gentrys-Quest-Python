# game packages
# entity packages
from ..Weapon.Weapon import Weapon
from ..Stats.Experience import Experience

class Enemy:
    """
    makes an enemy

    parameters

    name: string
        the name of the enemy

    health: int
        the health points

    attack: int
        the attack points

    defense: int
        the defense points

    weapon: Weapon
        the weapon that the enemy will carry

    description: string
        the description of the enemy
    """

    def __init__(self, name="enemy", health=1, attack=1, defense=1, weapon=Weapon(), description=None, experience=Experience()):
        super().__init__(name, None, description, experience)
        self.health = health
        self.attack = attack
        self.defense = defense
        self.weapon = weapon
