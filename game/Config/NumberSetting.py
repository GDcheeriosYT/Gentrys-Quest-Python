from .Setting import Setting


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

    def change_value(self, num):
        if num < max_value and num > min_value:
            self.value = num

    def __repr__(self):
        return f"{super()} <{self.value}>"
