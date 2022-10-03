# game packages
# Interface packages
from Interface.Interface import Interface
from Interface.InterfaceContent import InterfaceContent

# Content packages
from Content.Settings.GameSettings import GameSettings


class SettingsInterface(Interface):
    def __init__(self):
        super().__init__("settings", False, InterfaceContent("", ["travel", "inventory"]))

    def __repr__(self):
        action = self.visit()
