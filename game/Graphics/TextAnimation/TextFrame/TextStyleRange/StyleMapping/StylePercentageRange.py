class StylePercentageRange:
    """
    Makes a range of the percentage for the style

    parameters

    start: int
        the starting percentage of the range

    end: int
        the ending percentage of the range
    """

    start = None
    end = None

    def __init__(self, start=0, end=100):
        self.start = start
        self.end = end

    def __repr__(self):
        return self.start, self.end
