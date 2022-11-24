# game packages
# config packages
from .Setting import Setting

# IO packages
from IO import Window

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

    def __init__(self, name="", selected_value="nothing", settings=["nothing"]):
        super().__init__(name)
        self.selected_value = selected_value
        self.settings = settings

    def select(self):
        while True:
            string = ""
            QuestionText("select one").display()
            for setting in self.settings:
                string += f"{self.settings.index(setting) + 1}. {setting}\n"

            try:
                num = int(input(f"{string}{len(self.settings) + 1}. back\n")) - 1
                self.selected_value = self.settings[num]
                break
            except ValueError:
                Window.clear()
                WarningText("not a number!").display()
            except IndexError:
                Window.clear()
                break

    def __repr__(self):
        return f"{self.name} ↓[{self.selected_value}]↓"
