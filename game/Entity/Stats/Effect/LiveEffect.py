# game packages
# entity packages
from .EffectVariables import EffectVariables
from .EffectDetails import EffectDetails
from Entity.Entity import Entity
from Entity.Character.Character import Character
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.StatTypes import StatTypes

class LiveEffect:
    def __init__(self, details: EffectDetails, variables: EffectVariables):
        self.counter = 0
        self.details = details
        self.variables = variables


    def effect(self, turn: int, entity: Entity):
        if turn % self.variables.round_cooldown:
            self.counter += self.variables.lasts

        if self.counter > 0:
            for stat_collection in self.variables.stat_collection.content:
                try:
                    if stat_collection.stat == "StatTypes.Health":

                    if stat_collection.stat == "StatTypes.Health":
                    if stat_collection.stat == "StatTypes.Health":
                    if stat_collection.stat == "StatTypes.Health":
                    if stat_collection.stat == "StatTypes.Health":

