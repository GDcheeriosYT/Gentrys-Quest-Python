# game packages
# effect packages
from .EffectDetails import EffectDetails


class Effect:
    def __init__(self, details: EffectDetails):
        self.details = EffectDetails

    def effect(self):
        print(f"{self.details.name} did something...")
        return 0