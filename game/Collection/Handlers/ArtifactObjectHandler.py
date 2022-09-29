# game packages
# entity packages
from Entity.Stats.StatTypes import StatTypes
from Entity.Stats.Buff import Buff
from Entity.Stats.Experience import Experience
from Entity.Stats.StarRating import StarRating
from Entity.Artifact.Artifact import Artifact

# collection packages
from .BuffArrayHandler import BuffArrayHandler
from .ExperienceObjectHandler import ExperienceObjectHandler


class ArtifactObjectHandler:
    """
    Makes a Handler of a BuffArray

    parameters

    artifact_object: Object
        the artifact info
    """

    artifact_object = None

    def __init__(self, artifact_object):
        self.artifact_object = artifact_object

    def create_artifact(self):
        attributes = []
        for buff in self.artifact_object["stats"]["attributes"]:
            attributes.append(BuffArrayHandler(buff["buff"]).create_buff())
        return Artifact(
            name=self.artifact_object["name"],
            star_rating=StarRating(self.artifact_object["star rating"]),
            family=self.artifact_object["family"],
            main_attribute=BuffArrayHandler(self.artifact_object["stats"]["main attribute"]).create_buff(),
            attributes=attributes,
            experience=ExperienceObjectHandler(self.artifact_object["experience"]).create_experience()
        )
