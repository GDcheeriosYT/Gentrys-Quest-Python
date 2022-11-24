# game packages
# config packages
from .Setting import Setting

# graphics packages
from Graphics.Content.Text.QuestionText import QuestionText
from Graphics.Content.Text.WarningText import WarningText


class ClassSetting(Setting):
    """
    child of Setting.
    returns a class setting

    parameters

    class: Class
        class to edit
    """

    instance_class = None

    def __init__(self, name="setting", instance_class=None):
        super().__init__(name)
        self.instance_class = instance_class

    def __repr__(self):
        return f"{self.name}: {type(self.instance_class)}"
