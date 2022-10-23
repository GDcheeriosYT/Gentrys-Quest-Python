# game packages
# collection packages
from Collection.ItemList import ItemList

# graphics packages
from Graphics.TextAnimation.TextFrame.RangeList import RangeList

# config packages
from Config.ClassSetting import ClassSetting
from Config.SettingManager import SettingManager

# IO packages
from IO import Window


class RangeCollection:
    amount = None
    ranges = None

    def __init__(self, amount=1):
        self.ranges = ItemList(amount, RangeList, False)
        self.settings = [
            ClassSetting("ranges", self.ranges)
        ]

    def change_amount(self, amount):
        self.ranges.change_limit(amount)

    def test(self):
        Window.clear()
        self.settings = SettingManager(self.settings).config_settings()
        self.ranges = self.settings[0].instance_class
