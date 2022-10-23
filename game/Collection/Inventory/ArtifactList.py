# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs

# collection packages
from ..Handlers.ArtifactObjectHandler import ArtifactObjectHandler

# graphics packages
from Graphics.Status import Status

# built-in packages
import time


class ArtifactList:
    """
    Makes a list of artifacts

    parameters:
    artifacts: list
        the list of artifacts
    """

    artifacts = None

    def __init__(self, artifacts=[]):
        load_data_status = Status("Loading your artifact data", "dots")
        load_data_status.start()
        self.artifacts = []
        for artifact in artifacts:
            self.artifacts.append(ArtifactObjectHandler(artifact).create_artifact())
            #time.sleep(0.1)

        load_data_status.stop()