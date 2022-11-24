from .Setting import Setting


class ToggleSetting(Setting):
    """
    child of Setting.
    returns a toggleable setting

    parameters

    toggled: boolean
        if setting should be toggled or not
    """

    toggled = None

    def __init__(self, name="setting", toggled=False):
        super().__init__(name)
        self.toggled = toggled

    def toggle_setting(self):
        if self.toggled:
            self.toggled = False
        else:
            self.toggled = True

    def __repr__(self):
        return f"{self.name} [{self.toggled}]"
