# game packages
# config packages
from .Setting import Setting

# graphics packages
from Graphics.Content.Text.QuestionText import QuestionText
from Graphics.Content.Text.WarningText import WarningText


class NumberSetting(Setting):
    """
    child of Setting.
    returns a number setting

    parameters

    value: int
        value of setting
    """

    value = None
    min_value = None
    max_value = None

    def __init__(self, name="setting", value=0, min_value=-99999999, max_value=99999999):
        super().__init__(name)
        self.value = value,
        self.min_value = min_value
        self.max_value = max_value

    def change_value(self):
        while True:
            QuestionText(f"Please enter a value in between {min_value} and {max_value}").display()
            try:
                num = int(input())

                if max_value > num > min_value:
                    self.value = num
                    break
                elif num > max_value:
                    WarningText("Too big!").display()
                else:
                    WarningText("Too small!").display()

            except ValueError:
                WarningText("Bro, that's not even a number...")


    def __repr__(self):
        return f"{self.name} <{self.value}>"
