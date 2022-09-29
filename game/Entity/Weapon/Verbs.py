class Verbs:
    """
    Makes verbs for a weapon

    parameters

    normal: string
        the normal attack verb

    critical: string
        the critical attack verb
    """

    normal = None
    critical = None

    def __init__(self, normal, critical):
        self.normal = normal
        self.critical = critical