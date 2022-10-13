# game packages
# graphics packages
from Graphics.Text.Text import Text
from Graphics.Content.Text.WarningText import WarningText

# IO packages
from IO import Window

# config packages
from Config.ToggleSetting import ToggleSetting
from Config.NumberSetting import NumberSetting
from Config.StringSetting import StringSetting
from Config.ListSetting import ListSetting


class SettingManager:
    """
    A manager for setting configuration

    parameters

    settings: json_object
        the settings for this to manage
    """

    settings = None

    def __init__(self, settings):
        self.settings = settings

    def config_settings(self, loop=True):
        if loop:
            while True:
                Text("settings").display()
                for setting in self.settings:
                    Text(f"{self.settings.index(setting) + 1} {setting}").display()
                Text(f"{len(self.settings) + 1}. back").display()
                try:
                    value = int(input())
                    setting = self.settings[value - 1]
                    if isinstance(setting, ToggleSetting):
                        setting.toggle_setting()
                    elif isinstance(setting, NumberSetting):
                        setting.change_value()
                    elif isinstance(setting, StringSetting):
                        setting.change()
                    elif isinstance(setting, ListSetting):
                        setting.select()
                    else:
                        setting.instance_class.test()
                    self.settings[value - 1] = setting
                    Window.clear()
                except ValueError:
                    Window.clear()
                    WarningText("Not a number!").display()
                except IndexError:
                    Window.clear()
                    break

            if self.settings is not None:
                return self.settings
        else:
            Text("settings").display()
            for setting in self.settings:
                Text(f"{self.settings.index(setting) + 1} {setting}").display()
            Text(f"{len(self.settings) + 1}. back").display()
            try:
                value = int(input())
                if value == len(self.settings) + 1:
                    return None + ""  # causing a TypeError to end the while loop
                setting = self.settings[value - 1]
                if isinstance(setting, ToggleSetting):
                    setting.toggle_setting()
                elif isinstance(setting, NumberSetting):
                    setting.change_value()
                elif isinstance(setting, StringSetting):
                    setting.change()
                elif isinstance(setting, ListSetting):
                    setting.select()
                else:
                    setting.instance_class.test()
                self.settings[value - 1] = setting
                Window.clear()
            except ValueError:
                Window.clear()
                WarningText("Not a number!").display()
            except IndexError:
                Window.clear()

            if self.settings is not None:
                return self.settings
