# game packages
# Interface packages
from Interface.Interface import Interface
from Interface.InterfaceContent import InterfaceContent

# Content packages
from Content.Settings.GameSettings import GameSettings

# config packages
from Config.SettingManager import SettingManager

# IO packages
from IO import Window

class SettingsInterface:

    setting_manager = None

    def __init__(self, game_data):
        self.setting_manager = SettingManager(game_data.settings)

    def visit(self):
        return self.setting_manager.config_settings()