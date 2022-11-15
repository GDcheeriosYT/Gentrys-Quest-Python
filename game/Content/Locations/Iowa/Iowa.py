# game packages
# location packages
from Location.Location import Location

# content packages
from .BraydensHouse.BraydensHouse import BraydensHouse
from .CartersHouse.CartersHouse import CartersHouse


class Iowa(Location):
    def __init__(self):
        super().__init__(
            "Iowa",
            [
                BraydensHouse(),
                CartersHouse()
            ]
        )