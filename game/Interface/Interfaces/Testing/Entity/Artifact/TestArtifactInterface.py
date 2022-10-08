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
from Config.SettingManager import SettingManager


import random

class TestArtifactInterface:

    artifact = None
    settings = None

    def __init__(self, level=1, star_rating=1, main_attribute=Buff(), attributes=[]):
        name = get_random_name(False)
        experience = Experience(level)
        self.artifact=Artifact(name, StarRating(star_rating), None, Buff(), [], Experience())
        self.settings = [
            StringSetting("name", name),
            NumberSetting("star rating", star_rating, 1, 5),
            NumberSetting("level", experience.level, 1)
        ]

    def __repr__(self):
        Text(self.artifact).display()
        self.settings = SettingManager(self.settings).config_settings()
        self.artifact.name = self.settings[0].text
        self.artifact.star_rating = StarRating(self.settings[1])
        self.artifact.experience.level = self.settings[2]
