# game packages
# graphics packages
from Graphics.TextAnimation.TextAnimation import TextAnimation
from Graphics.Text.Text import Text


class EffectDetails:
    def __init__(self, name: str, text_animation: TextAnimation, description: str):
        self.name = Text(name)
        self.text_animation = text_animation
        self.description = Text(description)

    def show_details(self):
        Text(f"{self.name.content}\n{self.description}").display()