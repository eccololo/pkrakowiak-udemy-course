# Zaimplementuj klasę Weather, która ma dwa atrybuty instancji: temperature i humidity, które są inicjowane w metodzie konstruktora __init__(). W klasie Weather zaimplementuj również metodę statyczną celsius_to_fahrenheit(), która pobiera temperaturę w stopniach Celsjusza i zwraca równoważną temperaturę w stopniach Fahrenheita. Pamiętaj, że metoda ta ma być metodą statyczną.
#
#
#
# Uwaga! W celu zaliczenia ćwiczenia należy tylko zaimplementować klasę. Nie trzeba niczego drukować do konsoli. Testy jednostkowe sprawdzają poprawność implementacji rozwiązania.

class Weather:

    def __init__(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32


print(Weather.celsius_to_fahrenheit(20))
