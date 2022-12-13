# game packages
# location packages
from Location.Location import Location

# content packages
from .OhioZooAndAquarium.OhioZooAndAquarium import OhioZooAndAquarium


class Ohio(Location):
    def __init__(self):
        super().__init__(
            "Ohio",
            [
                OhioZooAndAquarium(),
            ]
        )
