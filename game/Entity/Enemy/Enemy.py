# game packages
# entity packages
from ..Entity import Entity
from ..Weapon.Weapon import Weapon
from ..Stats.Experience import Experience

# config packages
from Config.StringSetting import StringSetting
from Config.NumberSetting import NumberSetting
from Config.ClassSetting import ClassSetting
from Config.SettingManager import SettingManager

# IO packages
from IO import Window
from IO.Input import enter_to_continue

# random packages
from Random.Functions import determine_crit

# graphics packages
from Graphics.Text.Text import Text

# built-in packages
import random

class Enemy(Entity):
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

    def __init__(self, name="enemy", health=0, attack=0, defense=0, weapon=Weapon(), description=None,
                 experience=Experience()):
        super().__init__(name, description, 0, experience)
        self.health = None
        self.attack = None
        self.defense = None
        self.health_points = health
        self.attack_points = attack
        self.defense_points = defense
        self.weapon = weapon
        self.settings = [
            StringSetting("name", self.name),
            NumberSetting("health", self.health_points, 0),
            NumberSetting("attack", self.attack_points, 0),
            NumberSetting("defense", self.defense_points, 0),
            ClassSetting("weapon", self.weapon),
            StringSetting("description", self.description),
            NumberSetting("level", self.experience.level)
        ]
        self.update_stats()

    def update_stats(self):
        self.health = int(self.health_points * self.check_minimum(self.experience.level, 3) + (self.check_minimum(self.experience.level) * (self.check_minimum(self.experience.level / 20, 8))) + 20)
        self.attack = int(self.attack_points * self.check_minimum(self.experience.level, 2) + (self.check_minimum(self.experience.level, 0.5) * (self.check_minimum(self.experience.level / 20, 3))) + 2)
        self.defense = int(self.defense_points * self.check_minimum(self.experience.level, 1.5) + (self.check_minimum(self.experience.level, 0.3) * (self.check_minimum(self.experience.level / 20, 1.5))) + 1)

    def attack_character(self, character):
        is_crit = determine_crit(20)
        damage = int(self.attack + ((self.attack * 0.25) if is_crit else 0) - random.randint(0, character.defense))
        Text(f"{self.name} {self.weapon.verbs.critical if is_crit else self.weapon.verbs.normal} {character.name} for {damage} damage").display()
        if damage <= 0:
            Text(f"{character.name} has dodged").display()
        else:
            character.health -= damage
        enter_to_continue()

    def get_money(self):
        money = 0
        money += self.defense_points * 1.5
        money += self.attack_points * 2.5
        money += self.health_points * 2
        money += self.experience.level
        return int(money)

    def get_xp(self):
        xp = 0
        xp += self.defense_points * 0.5
        xp += self.attack_points * 1.5
        xp += self.health_points * 1
        xp += self.experience.level * 5
        return int(xp)

    def test(self):
        Window.clear()
        Text(self.__repr__()).display()
        self.show_stats()
        self.settings = SettingManager(self.settings).config_settings()
        self.name = self.settings[0].text
        self.health_points = self.settings[1].value
        self.attack_points = self.settings[2].value
        self.defense_points = self.settings[3].value
        self.weapon = self.settings[4].instance_class
        self.description = self.settings[5].text
        self.experience.level = self.settings[6].value
        self.update_stats()
        return self

    def show_stats(self):
        Text(f"health: {self.health}\n"
             f"attack: {self.attack}\n"
             f"defense {self.defense}\n"
             f"{self.description}\n").display()

    def __repr__(self):
        return f"{self.name} level {self.experience.level}"
