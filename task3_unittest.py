import unittest
from unittest.mock import patch
from task3 import StringBuilder, AppendCommand, StringBuilderListener

class TestStringBuilder(unittest.TestCase):
    def setUp(self):
        self.builder = StringBuilder()
        self.listener = StringBuilderListener()
        self.builder.add_listener(self.listener)

    def test_append_notifies_listener(self):
        with patch("builtins.print") as mock_print:
            self.builder.append("Hello, ")
            mock_print.assert_called_with("StringBuilder state changed: Hello, ")

    def test_undo_notifies_listener(self):
        with patch("builtins.print") as mock_print:
            self.builder.append("Hello, ")
            self.builder.undo()
            mock_print.assert_called_with("StringBuilder state changed: ")

    def test_undo_multiple_times_notifies_listener(self):
        with patch("builtins.print") as mock_print:
            self.builder.append("Hello, ")
            self.builder.append("world!")
            self.builder.undo()
            mock_print.assert_called_with("StringBuilder state changed: Hello, ")
            self.builder.undo()
            mock_print.assert_called_with("StringBuilder state changed: ")

if __name__ == "__main__":
    unittest.main()
