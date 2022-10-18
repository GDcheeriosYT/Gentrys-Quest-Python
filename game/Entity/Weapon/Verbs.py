# game packages
# config packages
from Config.StringSetting import StringSetting
from Config.SettingManager import SettingManager

# IO packages
from IO import Window

# mariachis packages
from Graphics.Text.Text import Text

class Verbs:
    """
    Makes verbs for a weapon

    parameters

    normal: string
        the normal attack verb

    critical: string
        the critical attack verb
    """

    normal = None
    critical = None

    def __init__(self, normal, critical):
        self.normal = normal
        self.critical = critical
        self.settings = [
            StringSetting("normal", self.normal),
            StringSetting("critical", self.critical),
        ]

    def __repr__(self):
        return (
f"""
player {self.normal} enemy        
player {self.critical} enemy        
""")

    def test(self):
        Window.clear()
        Text(self.__repr__()).display()
        self.settings = SettingManager(self.settings).config_settings(True)
        self.normal = self.settings[0].text
        self.critical = self.settings[1].text
        return Text(self)
