# game packages
# graphics packages
from Graphics.Text.Text import Text


class Location:
    """
    Makes a location.

    parameters:

    name: Text
        the name of the location
    """

    name = None
    areas

    def __init__(self, name=Text("location")):
        self.name = name

    def __repr__(self):
        return ""
