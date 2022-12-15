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

        Text(f"{len(self.areas) + 1}. back").display()

    def select_area(self, character, inventory, content):
        choice = get_int("Select an area") - 1
        try:
            self.areas[choice].start(character, inventory, content)
        except IndexError:
            pass

    def __repr__(self):
        return f"{self.name.raw_output()} {len(self.areas)} battle areas"
