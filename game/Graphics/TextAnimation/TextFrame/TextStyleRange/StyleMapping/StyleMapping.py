# game packages
# graphics packages
from StylePercentageRange import StylePercentageRange
from .....Text.Style import Style


class StyleMapping:
    """
    Makes a mapping for style in with a given percentage

    parameters

    percent_range: StylePercentageRange
        the percentage of the text for the style to apply to

    style: Style
        the style for that percent range of the text
    """

    percent_range = None
    style = None

    def __init__(self, percent_range=StylePercentageRange(), style=Style()):
        self.percent_range = percent_range
        self.style = style

    def __repr__(self):
        return self.percent_range, self.style
