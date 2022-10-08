# game packages
# config packages
from .Setting import Setting

# graphics packages
from Graphics.Content.Text.QuestionText import QuestionText
from Graphics.Content.Text.WarningText import WarningText


class NumberSetting(Setting):
    """
    child of Setting.
    returns a class setting

    parameters

    class: Class
        class to edit
    """

    value = None
    min_value = None
    max_value = None

    def __init__(self, instance_class, name="setting"):
        super().__init__(name)
        self.instance_class = instance_class

    def __repr__(self):
        return f"class: {Type(self.instance_class)}"
