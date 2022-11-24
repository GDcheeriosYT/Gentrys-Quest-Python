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

    def __init__(self, name="setting", value=0, min_value=None, max_value=None):
        super().__init__(name)
        self.value = value
        self.min_value = min_value
        self.max_value = max_value

    def change_value(self):
        while True:
            QuestionText(f"Please enter a value in between {'-unlimited' if self.min_value is None else self.min_value} and {'unlimited' if self.max_value is None else self.max_value}").display()
            try:
                num = int(input())
                if self.max_value is None and self.min_value is None:
                    self.value = num
                    break

                elif self.min_value is None:
                    if num <= self.max_value:
                        self.value = num
                        break
                    else:
                        WarningText("Too big!").display()

                elif self.max_value is None:
                    if num >= self.min_value:
                        self.value = num
                        break
                    else:
                        WarningText("Too small!").display()

            except ValueError:
                WarningText("Bro, that's not even a number...").display()

    def __repr__(self):
        return f"{self.name} <{self.value}>"
