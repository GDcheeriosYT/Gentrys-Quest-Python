# game packages
# entity packages
from .EffectVariables import EffectVariables
from .EffectDetails import EffectDetails
from Entity.Entity import Entity
from Entity.Character.Character import Character
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.StatTypes import StatTypes
from Entity.Stats.StatCollection import StatCollection
from Entity.Stats.StatValueTypes import StatValueTypes


class LiveEffect:
    def __init__(self, details: EffectDetails, variables: EffectVariables):
        self.counter = 0
        self.details = details
        self.variables = variables

    def affect(self, entity: Entity):
        try:
            stat_list = []
            if isinstance(entity, Enemy):
                stat_list = entity.get_stats()
            elif isinstance(entity, Character):
                stat_list = entity.get_stats()

            if self.counter > 0:
                for stat_collection in self.variables.stat_collection.content:
                    for stat in stat_list:
                        if stat.type == stat_collection.stat:
                            stat.total_value += stat_collection.value

        except Exception as e:
            print(e)
