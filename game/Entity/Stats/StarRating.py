# game packages
# graphics packages
from Graphics.Text.Text import Text
from Graphics.Text.Style import Style


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
        self.value = value

    def __repr__(self):
        if self.value == 1:
            return Text("★☆☆☆☆").raw_output()
        elif self.value == 2:
            return Text("★★☆☆☆", Style(text_color="green4")).raw_output()
        elif self.value == 3:
            return Text("★★★☆☆", Style(text_color="bright_blue")).raw_output()
        elif self.value == 4:
            return Text("★★★★☆", Style(text_color="magenta")).raw_output()
        else:
            return Text("★★★★★", Style(text_color="gold1")).raw_output()
