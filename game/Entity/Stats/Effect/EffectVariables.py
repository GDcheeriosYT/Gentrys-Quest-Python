# game packages
# entity packages
#from

# collection packages
from Collection.ItemList import ItemList


class EffectVariables:
    """
    The container class for Effect variables

    target_is_self: bool
        the way to tell if an effect will affect user or opponent

    lasts: int
        how many rounds an effect will last

    round_cooldown: int
        the cooldown before the effect is applied again

    stat_collections: ItemList
        the collection of stats and details about how they are affected
    """

    def __init__(self, target_is_self: bool, lasts: int, round_cooldown: int, stat_collection: ItemList):
        self.target_is_self = target_is_self
        self.lasts = lasts
        self.round_cooldown = round_cooldown
        self.stat_collection = stat_collection

    def get_target_string(self):
        if self.target_is_self:
            return "user"
        else:
            return "opponent"
