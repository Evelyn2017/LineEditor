
class invoker:
    def __init__(self, cmd):
        self.action = cmd

    def doaction(self):
        self.action.execute()

    def actionundo(self):
        self.action.undo()

    def actionredo(self):
        self.action.redo()