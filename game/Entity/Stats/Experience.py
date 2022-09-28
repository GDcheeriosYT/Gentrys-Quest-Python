class Experience:
    """
    experience for an Entity object

    parameters

    xp, xp_required, level: int
        values for experience
    """

    xp = None
    xp_required = None
    level = None

    def __init__(self, level=1, xp=0, xp_required=100):
        self.level = level,
        self.xp = xp
        self.xp_required = xp_required
