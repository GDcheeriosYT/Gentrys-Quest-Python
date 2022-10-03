# game packages
# Interface packages
from Interface.Interface import Interface
from Interface.InterfaceContent import InterfaceContent

# Content packages
from Content.Settings.GameSettings import GameSettings

# config packages
from Config.ToggleSetting import ToggleSetting
from Config.NumberSetting import NumberSetting
from Config.StringSetting import StringSetting

# IO packages
from IO import Window

class SettingsInterface(Interface):
    def __init__(self, settings):
        setting_list = []
        for setting in settings:
            key = setting
            value = settings[key]
            if isinstance(value, bool):
                setting_list.append(ToggleSetting(key, value))
            elif isinstance(value, int):
                setting_list.append(NumberSetting(key, value))
            else:
                setting_list.append(StringSetting(key, value))

        self.settings_size = len(setting_list)

        super().__init__("settings", False, InterfaceContent("", setting_list))

    def __repr__(self):
        while True:
            action = self.visit()
            if action < self.settings_size:
                setting = self.content.options[action]
                print(setting)
                if isinstance(setting, ToggleSetting):
                    setting.toggle_setting()
                elif isinstance(setting, NumberSetting):
                    setting.change_value()
                else:
                    setting.change()

                self.content.options[action] = setting
            else:
                Window.clear()
                break