# Zaimplementuj klase AirQualityMeasurement ktora obliczy srednia jakość powietrza, z wprowadzonych probek.

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
