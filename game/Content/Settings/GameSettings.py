from Config.ToggleSetting import ToggleSetting
from Config.NumberSetting import NumberSetting
from Config.StringSetting import StringSetting


class GameSettings:
    def __init__(self):
        self.settings = []
        self.settings.append(ToggleSetting("debug", False))
        self.settings.append(ToggleSetting("no timeout", False))
