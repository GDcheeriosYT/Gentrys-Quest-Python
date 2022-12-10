# game packages
# effect packages
from .EffectDetails import EffectDetails
from .EffectVariables import EffectVariables

# entity packages
from Entity.Stats.Experience import Experience


class Effect:
    def __init__(self, details: EffectDetails, variables: EffectVariables):
        self.details = details
        self.variables = variables
        self.experience = Experience()

