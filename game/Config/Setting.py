class Setting:
    """
    Makes a setting

    parameters

    name: string
        the name of the setting
    """

    name = None

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name
