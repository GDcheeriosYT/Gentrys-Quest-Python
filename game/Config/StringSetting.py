# game packages
# config packages
from .Setting import Setting

# graphics packages
from Graphics.Content.Text.QuestionText import QuestionText


class StringSetting(Setting):
    """
    child of Setting.
    returns a string setting

    parameters

    text: string
        the text the setting holds
    """

    def __init__(self, name="setting", text="Setting Text"):
        super().__init__(name)
        self.text = text

    def change(self):
        QuestionText("Please enter some text").display()
        self.text = input()

    def __repr__(self):
        return f"{self.name}: {self.text}"
