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
            return Text(f"*").raw_output()
        elif self.value == 2:
            return Text(f"**[white]", Style(text_color="green4")).raw_output()
        elif self.value == 3:
            return Text(f"***[white]", Style(text_color="bright_cyan")).raw_output()
        elif self.value == 4:
            return Text(f"****[white]", Style(text_color="bright_magenta")).raw_output()
        else:
            return Text(f"*****[white]", Style(text_color="bright_yellow")).raw_output()
