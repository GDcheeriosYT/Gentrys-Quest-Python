# game packages
# location packages
from Location.Location import Location

# content packages
from .BraydensHouse.BraydensHouse import BraydensHouse
from .CartersHouse.CartersHouse import CartersHouse
from .UnifinishedConstructionSite.UnfinishedConstructionSite import UnfinishedConstructionSite
from .DownTown.DownTown import DownTown
from .Target.Target import Target
from .ClimbIowa.ClimbIowa import ClimbIowa
from .ValleyHighSchool.ValleyHighSchool import ValleyHighSchool
from .HyVee.HyVee import HyVee

class Iowa(Location):
    def __init__(self):
        super().__init__(
            "Iowa",
            [
                BraydensHouse(),
                CartersHouse(),
                UnfinishedConstructionSite(),
                DownTown(),
                Target(),
                ValleyHighSchool(),
                ClimbIowa(),
                HyVee()
            ]
        )
