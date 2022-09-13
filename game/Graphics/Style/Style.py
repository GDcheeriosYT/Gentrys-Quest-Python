class Style:
    '''
    Contains all the styling info necessary for creating a Text object

    returns: style info

    parameters
    background_color: string
        the color of the background

    text_color: string
        the color of the text(foreground color)

    text_style: list
        contains the style(s) that the text will use.
        example ["bold", "underline"]
        example ["itallic"]
        can contain none or all 3 of those.
    '''

    background_color = "black"
    text_color = "white"
    text_style = []

    def __init__(self, background_color, text_color, text_style):
        self.background_color = background_color
        self.text_color = text_color
        self.text_style = text_style

    def get_style(self):
