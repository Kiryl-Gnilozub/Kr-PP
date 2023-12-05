import unittest
from task5 import fill, SquareFunction


class TestFillMethod(unittest.TestCase):
    def test_fill_method_with_negative_values(self):
        array = [None] * 5
        fill(array, SquareFunction())
        self.assertEqual(array, [0, 1, 4, 9, 16])

    def test_fill_method_with_zero_values(self):
        array = [None] * 3
        fill(array, SquareFunction())
        self.assertEqual(array, [0, 1, 4])

    def test_fill_method_with_large_array(self):
        array = [None] * 10
        fill(array, SquareFunction())
        self.assertEqual(array, [0, 1, 4, 9, 16, 25, 36, 49, 64, 81])

    def test_fill_method_with_custom_function(self):
        class CubeFunction:
            def apply(self, value):
                return value ** 3

        array = [None] * 4
        fill(array, CubeFunction())
        self.assertEqual(array, [0, 1, 8, 27])


if __name__ == '__main__':
    unittest.main()
