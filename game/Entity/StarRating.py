# game packages
# graphics packages
from ..Graphics.Text.Text import Text
from ..Graphics.Text.Style import Style

# external packages

class StarRating:
    """
    the star rating of an entity

    parameters

    value: int
        the value of the star rating
    """

    value = None

    def __init__(self, value=1):
        self.value = 1

    def __repr__(self):
        if self.value == 1:
            return Text("★☆☆☆☆").display()
        elif self.value == 2:
            return Text("★★☆☆☆", Style(text_color="green4")).display()
        elif self.value == 3:
            return Text("★★★☆☆", Style(text_color="bright_blue")).display()
        elif self.value == 4:
            return Text("★★★★☆", Style(text_color="magenta")).display()
        else:
            return Text("★★★★★", Style(text_color="gold1")).display()
