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

    def __init__(self, name="enemy", health=1, attack=1, defense=1, weapon=Weapon(), description=None,
                 experience=Experience()):
        super().__init__(name, description, 0, experience)
        self.health = health
        self.attack = attack
        self.defense = defense
        self.weapon = weapon
        self.settings = [
            StringSetting("name", self.name),
            NumberSetting("health", self.health),
            NumberSetting("attack", self.attack),
            NumberSetting("defense", self.defense),
            ClassSetting("weapon", self.weapon),
            StringSetting("description", self.description),
            NumberSetting("level", self.experience.level)
        ]

    def attack_character(self, character):
        is_crit = determine_crit(20)
        damage = int(self.attack + ((self.attack * 0.25) if is_crit else 0) - random.randint(0, character.defense))
        Text(f"{self.name} {self.weapon.verbs.critical if is_crit else self.weapon.verbs.normal} {character.name} for {damage}").display()
        if damage <= 0:
            Text(f"{character.name} has dodged").display()
        character.health -= damage
        enter_to_continue()

    def get_money(self):
        return self.experience.level

    def get_xp(self):
        return self.experience.level * 10

    def test(self):
        Window.clear()
        self.settings = SettingManager(self.settings).config_settings()
        self.name = self.settings[0].text
        self.health = self.settings[1].value
        self.attack = self.settings[2].value
        self.defense = self.settings[3].value
        self.weapon = self.settings[4].instance_class
        self.experience.level = self.settings[7].value
        return self

    def show_stats(self):
        Text(f"health: {self.health}\n"
             f"attack: {self.attack}\n"
             f"defense {self.defense}\n"
             f"{self.description}\n").display()

    def __repr__(self):
        return f"{self.name} level {self.experience.level}"
