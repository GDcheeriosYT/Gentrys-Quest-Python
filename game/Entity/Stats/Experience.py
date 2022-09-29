class Experience:
    """
    experience for an Entity object

    parameters

    xp, level: int
        values for experience
    """

    xp = None
    xp_required = None
    level = None

    def __init__(self, level=1, xp=0):
        self.level = level
        self.xp = xp

    def __repr__(self):
        return f"level {self.level} {self.xp}xp"
