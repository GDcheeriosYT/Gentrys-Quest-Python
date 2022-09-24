# game packages
# graphics packages
from TextStyleRange.TextStyleRange import TextStyleRange

class TextFrame:
    """
    Makes a frame to be used in a TextAnimation

    parameters

    text_style_range: TextStyleRange
        the text style range
    """

    text_style_range = None

    def __init__(self, text_style_range=TextStyleRange()):
        self.text_style_range = text_style_range
