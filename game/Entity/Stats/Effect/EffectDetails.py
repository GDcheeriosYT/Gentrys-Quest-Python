# game packages
# graphics packages
from Graphics.TextAnimation.TextAnimation import TextAnimation
from Graphics.Text.Text import Text

# Entity packages
from Entity.Stats.StatTypes import StatTypes


class EffectDetails:
    def __init__(self, name: str, text_animation: TextAnimation, description: str):
        self.name = Text(name)
        self.text_animation = text_animation
        self.description = Text(description)
