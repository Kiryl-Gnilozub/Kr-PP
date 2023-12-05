class Command:
    def execute(self, target):
        pass

    def undo(self, target):
        pass


class AppendCommand(Command):
    def __init__(self, text):
        self.text = text

    def execute(self, target):
        target._execute(self)

    def undo(self, target):
        target._undo(self)


class StringBuilder:
    def __init__(self):
        self._string = ""
        self._undo_stack = []

    def _execute(self, command):
        self._string += command.text
        self._undo_stack.append(command)

    def _undo(self, command):
        self._string = self._string[:-len(command.text)]

    def append(self, text):
        command = AppendCommand(text)
        command.execute(self)

    def undo(self):
        if self._undo_stack:
            command = self._undo_stack.pop()
            command.undo(self)

    def __str__(self):
        return self._string


builder = StringBuilder()

builder.append("Hello, ")

print(builder)

builder.append("world!")

print(builder)

builder.undo()

print(builder)
