class RangeGroup:
    def __init__(self, start_index: int, end_index: int):
        self.start_index = start_index
        self.end_index = end_index
        self.exceptions = []

    def add_exception(self, index):
        if index in self.exceptions:
            self.exceptions.remove(index)
        else:
            self.exceptions.append(index)