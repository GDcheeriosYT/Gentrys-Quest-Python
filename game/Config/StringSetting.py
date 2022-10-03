from .Setting import Setting


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

    def __repr__(self):
        return f"{super()}: {self.text}"
