class StringBuilderListener:
    def update(self, subject):
        print(f"StringBuilder state changed: {subject}")


class AppendCommand:
    def __init__(self, text):
        self.text = text

    def execute(self, target):
        target._execute(self)

    def undo(self, target):
        target._undo(self)


class StringBuilder:
    def __init__(self):
        self._string = ""
        self._listeners = []
        self._undo_stack = []

    def add_listener(self, listener):
        self._listeners.append(listener)

    def remove_listener(self, listener):
        self._listeners.remove(listener)

    def notify_listeners(self):
        for listener in self._listeners:
            listener.update(self)

    def _execute(self, command):
        self._string += command.text
        self._undo_stack.append(command)
        self.notify_listeners()

    def _undo(self, command):
        if command in self._undo_stack:
            self._undo_stack.remove(command)
            self._string = "".join([c.text for c in self._undo_stack])
            self.notify_listeners()

    def append(self, text):
        command = AppendCommand(text)
        command.execute(self)

    def undo(self):
        if self._undo_stack:
            command = self._undo_stack[-1]
            command.undo(self)

    def __str__(self):
        return self._string


builder = StringBuilder()

listener = StringBuilderListener()

builder.add_listener(listener)

builder.append("Hello, ")

builder.append("world!")

builder.undo()

print(builder)
