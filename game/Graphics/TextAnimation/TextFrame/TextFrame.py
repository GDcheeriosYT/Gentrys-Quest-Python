# game packages
# collection packages
from Collection.ItemList import ItemList

# graphics packages
from .ColorCollection import ColorCollection
from .RangeCollection import RangeCollection

# config settings
from Config.NumberSetting import NumberSetting
from Config.ClassSetting import ClassSetting
from Config.SettingManager import SettingManager

# IO packages
from IO import Window


class TextFrame:
    """
    Makes a frame to be used in a TextAnimation

    parameters

    color_amount: int
        the amount of colors in this frame
    """

    color_amount = None
    colors = None
    range = None

    def __init__(self, color_amount=1):
        self.colors = ColorCollection(color_amount)
        self.ranges = RangeCollection(color_amount)
        self.settings = [
            NumberSetting("color amount", color_amount, 1),
            ClassSetting("colors", self.colors),
            ClassSetting("range", self.ranges)
        ]

    def test(self):
        Window.clear()
        self.settings = SettingManager(self.settings).config_settings()
        self.colors.change_amount(self.settings[0].value)
        self.range.change_amount(self.settings[0].value)
        self.colors.colors = self.settings[1].instance_class
        self.ranges.ranges = self.settings[2].instance_class
