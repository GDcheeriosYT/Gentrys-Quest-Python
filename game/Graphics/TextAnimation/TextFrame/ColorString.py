# game packages
# config settings
from Config.StringSetting import StringSetting
from Config.SettingManager import SettingManager

# IO packages
from IO import Window


class ColorString:
    string = None

    def __init__(self, string="white"):
        self.string = string
        self.settings = [
            StringSetting("string", self.string)
        ]

    def test(self):
        Window.clear()
        self.settings = SettingManager(self.settings).config_settings()
        self.string = self.settings[0]
