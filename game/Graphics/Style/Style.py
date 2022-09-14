class Style:
    """
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
    """

    background_color = None
    text_color = None
    text_style = None

    def __init__(self, background_color="black", text_color="white", text_style="[]"):
        self.background_color = background_color
        self.text_color = text_color
        self.text_style = text_style

    def __repr__(self):
        # creates a string of the styles using the options from the text style list
        style_string = ""
        for option in self.text_style:
            style_string += f"{option} "

        return f"[{self.text_color} on {self.background_color} {style_string[:-1]}]"  # [:-1] is to exclude the extra space at the end
