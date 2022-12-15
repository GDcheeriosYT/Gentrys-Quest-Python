# game packages
# entity packages
from Entity.Stats.StatTypes import StatTypes
from Entity.Stats.Buff import Buff
from Entity.Stats.Experience import Experience


class BuffArrayHandler:
    """
    Makes a Handler of a BuffArray

    parameters

    buff_array: list
        the array of 3 numbers
    """

    buff_array = None

    def __init__(self, buff_array=[0, 0, 0]):
        self.buff_array = buff_array

    def create_buff(self):
        if isinstance(self.buff_array, dict):
            self.buff_array = self.buff_array["buff"]
        return Buff(StatTypes(self.buff_array[0]), Experience(self.buff_array[2]), self.buff_array[1] == 1)
