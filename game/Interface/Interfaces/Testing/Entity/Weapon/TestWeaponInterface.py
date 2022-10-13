from Interface.Interface import Interface
from Interface.InterfaceContent import InterfaceContent

from Entity.Artifact.Artifact import Artifact
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

    weapon = none
    settings = none

    def __init__(self, name="fists", description="punches things", weapon_type=None, attack=3,
                 buff=Buff(StatTypes.Health, Experience(), False), verbs=None, star_rating=StarRating(), experience=Experience()):
        super().__init__(name, description, star_rating, experience)
        self.weapon_type = weapon_type
        self.attack = attack
        self.buff = buff
        self.verbs = verbs
        self.settings = [
            StringSetting("name", self.name),
            StringSetting("description", self.description),
            StringSetting("weapon_type", self.weapon_type),
            NumberSetting("attack", self.attack),
            ClassSetting("buff", self.buff),
            ClassSetting("verbs", self.verbs),
            NumberSetting("star_rating", self.star_rating),
            NumberSetting("experience", self.experience)
        ]







