class EditorInterface:
    """
    A class to edit things in :)

    parameters

    editing_class : class
        the class to edit
    """

    editing_class = None

    def __init__(self, editing_class):
        self.editing_class = editing_class()

    def edit(self):
        while True:
            self.editing_class.__repr__()
