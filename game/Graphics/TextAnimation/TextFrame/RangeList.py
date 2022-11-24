# game packages
# collection packages
from Collection.ItemList import ItemList

# config settings
from Config.NumberSetting import NumberSetting
from Config.SettingManager import SettingManager

# IO packages
from IO import Window

# graphics packages
from Graphics.Text.Text import Text


class RangeList:
    range = None

    def __init__(self):
        self.range = ItemList(2, int, False)
        self.range.content = [0, 100]
        self.settings = [
            NumberSetting("start%", self.range.content[0], 0, self.range.content[1]),
            NumberSetting("end%", self.range.content[1], self.range.content[0], 100)
        ]

    def test(self):
        Window.clear()
        Text(f"looking at {self.range.get(0)}% to {self.range.get(1)}%")
        self.settings = SettingManager(self.settings).config_settings()
        self.range.set(0, self.settings[0].value)
        self.range.set(1, self.settings[1].value)
