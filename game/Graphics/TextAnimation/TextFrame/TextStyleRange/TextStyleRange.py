# game packages
# graphics packages
from StyleMapping.StyleMapping import StyleMapping

class TextStyleRange:
    """
    Makes a text range

    parameters

    range: list
        the list of StyleMappings
    """

    range = None

    def __init__(self, range=StyleMapping()):
        self.range = range

    def __repr__(self):
        return self.range
