# game packages
# collection packages
from Collection.ItemList import ItemList

# config packages
from Config.ClassSetting import ClassSetting
from Config.SettingManager import SettingManager

# graphics packages
from .ColorString import ColorString

# IO packages
from IO import Window


class ColorCollection:
    amount = None
    colors = None

    def __init__(self, amount=1):
        self.colors = ItemList(amount, ColorString, False)
        self.settings = [
            ClassSetting("colors", self.colors)
        ]

    def change_amount(self, amount):
        self.colors.change_limit(amount)

    def test(self):
        Window.clear()
        self.settings = SettingManager(self.settings).config_settings()
        self.colors = self.settings[0].instance_class
