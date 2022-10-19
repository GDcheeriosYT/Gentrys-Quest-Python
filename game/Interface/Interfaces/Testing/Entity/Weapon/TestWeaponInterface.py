from Interface.Interface import Interface
from Interface.InterfaceContent import InterfaceContent

from Entity.Weapon.Weapon import Weapon
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes

from Graphics.Text.Text import Text

from Random.Functions import get_random_name

from Config.NumberSetting import NumberSetting
from Config.StringSetting import StringSetting
from Config.ToggleSetting import ToggleSetting
from Config.ClassSetting import ClassSetting
from Config.SettingManager import SettingManager

from IO import Window

import random

class TestWeaponInterface:

    weapon = None
    settings = None

    def __init__(self):
        self.weapon = Weapon()
        self.settings = [
            StringSetting("name", self.weapon.name),
            StringSetting("description", self.weapon.description),
            StringSetting("weapon_type", self.weapon.weapon_type),
            NumberSetting("attack", self.weapon.attack),
            ClassSetting("buff", self.weapon.buff),
            ClassSetting("verbs", self.weapon.verbs),
            NumberSetting("star_rating", self.weapon.star_rating.value, 1, 5),
            NumberSetting("experience", self.weapon.experience.level, 1)
        ]

    def __repr__(self):
        Window.clear()
        Text(self.weapon).display()
        self.settings = SettingManager(self.settings).config_settings()
        self.weapon.name = self.settings[0].text
        self.weapon.description = self.settings[1].text
        self.weapon.weapon_type = self.settings[2].text
        self.weapon.attack = self.settings[3].value
        self.weapon.buff = self.settings[4].instance_class
        self.weapon.verbs = self.settings[5].instance_class
        self.weapon.star_rating = StarRating(self.settings[6].value)
        self.weapon.experience.level = self.settings[7].value
        return self


