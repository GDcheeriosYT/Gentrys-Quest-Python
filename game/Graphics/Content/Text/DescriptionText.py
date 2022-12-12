# graphics game packages
from ...Text.Text import Text
from ...Text.Style import Style


class DescriptionText(Text):
    """
    makes a warning type of text

    parameters

    content: string
        the text that it will contain
    """

    content = None

    def __init__(self, content="text"):
        super().__init__(content, Style("black", "bright_green", ["italic"]))
