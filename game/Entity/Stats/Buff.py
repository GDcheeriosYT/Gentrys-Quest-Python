# game packages
# entity packages
from .StatTypes import StatTypes
from .Experience import Experience

# config packages
from Config.NumberSetting import NumberSetting
from Config.StringSetting import StringSetting
from Config.ToggleSetting import ToggleSetting
from Config.ClassSetting import ClassSetting
from Config.SettingManager import SettingManager

# IO packages
from IO import Window

# graphics packages
from Graphics.Text.Text import Text

# built-in packages
import random


class Buff:
    """
    Makes a buff for attributes

    parameters

    attribute_type: StatTypes
        the attribute for the buff to buff

    experience: Experience
        the experience of the buff

    is_percent: boolean
        determines if the buff is a percent type
    """

    attribute_type = None
    experience = None
    is_percent = None

    def __init__(self, attribute_type=None, experience=Experience, is_percent=random.choice([True, False])):
        if attribute_type is None:
            self.attribute_type = random.choice(list(StatTypes))
        else:
            self.attribute_type = attribute_type
        self.experience = experience
        self.is_percent = is_percent
        self.settings = [
            NumberSetting("level", self.experience.level, 1),
            ToggleSetting("is percent type", self.is_percent)
        ]

    def __repr__(self):
        return f"{self.attribute_type.name} 0{'%' if self.is_percent else ''}[{self.experience.level}]"

    def test(self):
        Window.clear()
        Text(self.__repr__()).display()
        self.settings = SettingManager(self.settings).config_settings(True)
        self.experience.level = self.settings[0].value
        self.is_percent = self.settings[1].toggled
        return Text(self)
