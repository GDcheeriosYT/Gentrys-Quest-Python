# game packages
# config packages
from Config.NumberSetting import NumberSetting
from Config.ClassSetting import ClassSetting
from Config.SettingManager import SettingManager

# collection packages
from Collection.ItemList import ItemList

# graphics packages
from .TextFrame.TextFrame import TextFrame
from ..Text.Text import Text

# IO packages
from IO import Window

class TextAnimation:
    """
    Makes an animation format for Text object

    parameters

    interval: int, double
        the interval between frames

    text_frames: list
        the list of TextFrames
    """

    interval = None
    text_frames = None

    def __init__(self, interval=0.3, frames=ItemList(content_type=TextFrame)):
        self.interval = interval
        self.frames = frames
        self.settings = [
            NumberSetting("interval", self.interval, 0.1, 100),
            ClassSetting("frames", self.frames)
        ]

    def get_json(self):
        animation_info = {
            "interval": self.interval * 1000,
            "frames": []
        }
        for frame in self.frames.content:
            animation_info["frames"].append({
                "colors": frame.colors,
                "range": frame.range
            })

    def test(self):
        Window.clear()
        self.settings = SettingManager(self.settings).config_settings()
        self.interval = self.settings[0].value
        self.frames = self.settings[1].instance_class
