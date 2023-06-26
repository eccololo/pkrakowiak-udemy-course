# Zaimplementuj klase Weather ktora zamieni stopnie Celcjusza na Fahrenheita.

class Weather:

    def __init__(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32


print(Weather.celsius_to_fahrenheit(20))
