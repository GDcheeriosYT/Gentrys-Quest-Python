# game packages
# graphics packages
from Graphics.Text.Text import Text

# IO packages
from IO.Input import get_int


class Location:
    """
    Makes a location.

    parameters:

    name: Text
        the name of the location
    """

    name = None
    areas = None

    def __init__(self, name: str, areas: list):
        self.name = Text(name)
        self.areas = areas

    def list_areas(self):
        for area in self.areas:
            Text(f"{self.areas.index(area) + 1}. {area}").display()

        Text(f"{}").display()

    def select_area(self):
        get_int("")

    def __repr__(self):
        return ""
