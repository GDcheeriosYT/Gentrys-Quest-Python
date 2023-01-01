# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs

# collection packages
from ..Handlers.ArtifactObjectHandler import ArtifactObjectHandler
from ..ItemList import ItemList

# graphics packages
from Graphics.Status import Status
from Graphics.Text.Text import Text

# entity packages
from Entity.Artifact.Artifact import Artifact

# IO packages
from IO.Input import get_int

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
            # time.sleep(0.1)

        load_data_status.stop()

    def give_item_list(self):
        return ItemList(content_type=Artifact, content=self.artifacts)
