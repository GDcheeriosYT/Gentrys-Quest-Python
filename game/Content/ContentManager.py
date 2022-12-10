# game packages
# content packages
from .ArtifactContentManager import ArtifactContentManager
from .LocationContentManager import LocationContentManager
from .CharacterContentManager import CharacterContentManager


class ContentManager:
    characters = None
    weapons = None
    families = None
    locations = None

    def __init__(self):
        artifact_content_manager = ArtifactContentManager()
        artifact_content_manager.load_content()
        location_content_manager = LocationContentManager()
        location_content_manager.load_content()
        character_content_manager = CharacterContentManager()
        character_content_manager.load_content()
        self.families = artifact_content_manager.get_families()
        self.locations = location_content_manager.get_locations()
        self.characters = character_content_manager.get_characters()

