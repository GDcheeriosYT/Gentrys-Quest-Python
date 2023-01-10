# game packages
# location packages
from Location.Location import Location

# content packages
from .BeiJing.BeiJing import BeiJing


class China(Location):
    def __init__(self):
        super().__init__(
            "China",
            [
                BeiJing()
            ]
        )
