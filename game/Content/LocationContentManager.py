# game packages
# content packages
from .Locations.Iowa.Iowa import Iowa
from .Locations.Nigeria.Nigeria import Nigeria
from .Locations.Ohio.Ohio import Ohio
from .Locations.China.China import China
from .Locations.GentrysHouse.GentrysHouse import GentrysHouseLocation

# graphics packages
from Graphics.Status import Status

# built-in packages
import importlib
import inspect
import os


class Location:
    def __init__(self, name):
        self.name = name
        self.areas = []


class LocationContentManager:
    families = None

    def __init__(self):
        self.locations = []

    def load_content(self):
        load_status = Status("Loading Game Locations...")
        load_status.start()
        self.locations = [
            Iowa(),
            Nigeria(),
            Ohio(),
            China(),
            GentrysHouseLocation()
        ]
        load_status.stop()

    def get_locations(self):
        return self.locations
