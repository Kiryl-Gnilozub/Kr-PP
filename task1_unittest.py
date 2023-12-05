import unittest
from task1 import BaseConverter, ConverterFactory, Locale


class TestTemperatureConverter(unittest.TestCase):
    def test_celsius_to_kelvin(self):
        converter = BaseConverter(0)
        result = converter.convert("kelvin")
        self.assertEqual(result, 273.15)

    def test_fahrenheit_conversion_for_supported_country(self):
        locale = Locale("US")
        converter = ConverterFactory.create_converter(locale)
        converter.temperature = 0
        result = converter.convert("fahrenheit")
        self.assertEqual(result, 32.0)

    def test_fahrenheit_conversion_for_unsupported_country(self):
        locale = Locale("RU")
        converter = ConverterFactory.create_converter(locale)
        converter.temperature = 0
        result = converter.convert("fahrenheit")
        self.assertEqual(result, 0.0)

    def test_fahrenheit_conversion_for_unsupported_country(self):
        locale = Locale("RU")
        converter = ConverterFactory.create_converter(locale)
        converter.temperature = 0
        result = converter.convert("fahrenheit")
        self.assertEqual(result, 0.0)


if __name__ == '__main__':
    unittest.main()
