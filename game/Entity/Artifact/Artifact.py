# game packages
# entity packages
from ..Entity import Entity
from ..Stats.Buff import Buff
from ..Stats.Experience import Experience
from ..Stats.StarRating import StarRating
from ArtifactFamily import ArtifactFamily

# collection packages
from ...Collection.ItemList import ItemList


class Artifact(Entity):
    """
    Makes an artifact

    parameters

    name: string
        the name of the Artifact

    description: string
        the description of the Artifact

    star_rating: StarRating
        the star rating of the Artifact

    family: ArtifactFamily
        the family that the Artifact is in

    main_attribute: Buff
        the main attribute of the Artifact

    attributes: list
        the attributes that this artifact has

    experience: Experience
        the experience of the Artifact
    """

    name = None
    description = None
    star_rating = None
    family = None
    main_attribute = None
    attributes = None
    experience = None

    def __init__(self, name, description="description", star_rating=StarRating(1), family=ArtifactFamily(), main_attributes=Buff(), attributes=[], experience=Experience()):
        super().__init__(name, description, star_rating, experience)
        self.family = family
        self.main_attribute = main_attributes
        self.attributes = attributes
