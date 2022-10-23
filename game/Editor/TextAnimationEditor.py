# game packages
# graphics packages
from Graphics.TextAnimation.TextAnimation import TextAnimation
from Graphics.Text.Text import Text

# IO packages
from IO import Window

# config packages
from Config.StringSetting import StringSetting
from Config.NumberSetting import NumberSetting
from Config.ClassSetting import ClassSetting
from Config.SettingManager import SettingManager


class TextAnimationEditor:
    text = None
    text_animation = None
    settings = None

    def __init__(self):
        self.text = Text("This is text!")
        self.text_animation = TextAnimation()
        self.settings = [
            StringSetting("text", self.text),
            ClassSetting("animation", self.text_animation)
        ]

    def __repr__(self):
        Window.clear()
        self.settings = SettingManager(self.settings).config_settings()
        self.text = self.settings[0].text
        self.text_animation = self.settings[1].instance_class
