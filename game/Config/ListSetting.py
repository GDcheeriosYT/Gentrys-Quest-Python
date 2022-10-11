# game packages
# config packages
from .Setting import Setting

# graphics packages
from Graphics.Content.Text.QuestionText import QuestionText
from Graphics.Content.Text.WarningText import WarningText


class ListSetting(Setting):
    """
    child of Setting.
    returns a number setting

    parameters

    value: int
        value of setting
    """

    settings = None

    def __init__(self, name="", settings=["nothing"]):
        super().__init__(name)
        self.settings = settings

    def select(self):
        QuestionText("select one").display()
        string = ""
        for setting in self.settings:
            string += f"{self.settings.index(setting) + 1}. {setting}"

        return self.settings[input(f"{string}\n{len(self.settings) + 1} back")]


    def __repr__(self):
        return f"{self.name} ={self.value}="
