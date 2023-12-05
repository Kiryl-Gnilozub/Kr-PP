class Locale:
    def __init__(self, country):
        self.country = country


fahrenheit_countries = {"BS", "US", "BZ", "KY", "PW"}


class BaseConverter:
    def __init__(self, temperature=0, country=""):
        self.temperature = temperature
        self.country = country

    def convert(self, to_unit):
        if to_unit == "kelvin":
            return self.temperature + 273.15
        elif to_unit == "fahrenheit":
            if self.country and self.country not in fahrenheit_countries:
                return 0.0
            return (self.temperature * 9/5) + 32


class ConverterFactory:
    @staticmethod
    def create_converter(locale):
        converter = BaseConverter()
        converter.country = locale.country
        return converter


if __name__ == "__main__":
    locale = Locale("US")
    converter = ConverterFactory.create_converter(locale)

    temperature_in_celsius = float(
        input("Введите температуру в градусах Цельсия: "))
    converter.temperature = temperature_in_celsius

    temperature_in_kelvin = converter.convert("kelvin")
    temperature_in_fahrenheit = converter.convert("fahrenheit")
    print(f"{temperature_in_celsius} градусов по Цельсию равны {temperature_in_kelvin} Кельвин и {temperature_in_fahrenheit} Фаренгейт.")
