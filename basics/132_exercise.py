# Załóżmy, że
# pracujesz
# nad
# projektem
# monitorowania
# jakości
# powietrza
# w
# mieście.Masz
# już
# utworzoną
# klasę
# AirQualityMeasurement
# do
# reprezentowania
# pomiarów
# jakości
# powietrza
# w
# określonej
# lokalizacji
# i
# śledzenia
# odczytów
# w
# czasie:
#
#
# class AirQualityMeasurement:
#     all_measurements = []
#
#     def __init__(self, location, aqi):
#         self.location = location
#         self.aqi = [aqi]
#         AirQualityMeasurement.all_measurements.append(self)
#
#     def add_aqi_reading(self, aqi):
#         self.aqi.append(aqi)
#
#
# Zaimplementuj
# metodę
# tej
# klasy
# o
# nazwie
# average_aqi(), która
# oblicza
# średni
# wskaźnik
# jakości
# powietrza(AQI)
# dla
# wszystkich
# monitorowanych
# lokalizacji
# zaokrąglony
# do
# drugiego
# miejsca
# po
# przecinku.
#
# Przykład
# użycia
# klasy
# AirQualityMeasurement:
#
# [IN]: measurement1 = AirQualityMeasurement('Downtown', 50)
# [IN]: measurement1.add_aqi_reading(45)
# [IN]: measurement1.add_aqi_reading(60)
#
# [IN]: measurement2 = AirQualityMeasurement('Suburb', 40)
# [IN]: measurement2.add_aqi_reading(30)
# [IN]: measurement2.add_aqi_reading(50)
#
# [IN]: AirQualityMeasurement.average_aqi()
#
# [OUT]: 45.83
#
# Uwaga! W
# celu
# zaliczenia
# ćwiczenia
# należy
# tylko
# zaimplementować
# metodę.Nie
# trzeba
# niczego
# drukować
# do
# konsoli.Testy
# jednostkowe
# sprawdzają
# poprawność
# implementacji
# rozwiązania.

class AirQualityMeasurement:
    all_measurements = []

    def __init__(self, location, aqi):
        self.location = location
        self.aqi = [aqi]
        AirQualityMeasurement.all_measurements.append(self)

    def add_aqi_reading(self, aqi):
        self.aqi.append(aqi)

    # Enter your solution here

    @classmethod
    def average_aqi(cls):
        avg_air_q = 0
        len_air_q = 0
        for mes in cls.all_measurements:
            avg_air_q += sum(mes.aqi)
            len_air_q += len(mes.aqi)

        return round(avg_air_q / len_air_q, 2)
