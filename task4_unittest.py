import unittest
from task4 import custom_filter, StringLengthFilter, NumberFilter


class TestFilterModule(unittest.TestCase):
    def test_string_length_filter(self):
        filter_instance = StringLengthFilter()
        input_array = ["apple", "banana", "grape", "orange"]

        result = custom_filter(input_array, filter_instance)

        self.assertEqual(result, ["banana", "orange"])

    def test_number_filter(self):
        filter_instance = NumberFilter()
        input_array = [15, 5, 20, "apple", "orange"]

        result = custom_filter(input_array, filter_instance)

        self.assertEqual(result, [15, 20])


if __name__ == '__main__':
    unittest.main()
