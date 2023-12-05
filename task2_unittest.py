import unittest
from task2 import StringBuilder


class TestStringBuilder(unittest.TestCase):
    def test_append(self):
        builder = StringBuilder()
        builder.append("Hello, ")
        builder.append("world!")
        self.assertEqual(str(builder), "Hello, world!")

    def test_undo(self):
        builder = StringBuilder()
        builder.append("Hello, ")
        builder.undo()
        self.assertEqual(str(builder), "")

    def test_undo_multiple(self):
        builder = StringBuilder()
        builder.append("Hello, ")
        builder.append("world!")
        builder.undo()
        self.assertEqual(str(builder), "Hello, ")

        builder.undo()
        self.assertEqual(str(builder), "")

    def test_undo_empty(self):
        builder = StringBuilder()
        builder.undo() 
        self.assertEqual(str(builder), "")


if __name__ == "__main__":
    unittest.main()
