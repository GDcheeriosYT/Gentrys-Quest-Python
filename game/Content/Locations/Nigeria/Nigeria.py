# game packages
# location packages
from Location.Location import Location

# content packages
from .PureTabooSet.PureTabooSet import PureTabooSet


class Nigeria(Location):
    def __init__(self):
        super().__init__(
            "Nigeria",
            [
                PureTabooSet()
            ]
        )