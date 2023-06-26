# [IN]: w = Weather('Warsaw', 23, 60)
# [IN]: print(w.report())
#
#
# [OUT]: The weather in Warsaw is currently:
#          - 23 degrees
#          - 60% humidity

# [IN]: w = SunnyWeather('Warsaw', 23, 60, 80)
# [IN]: print(w.report())
#
#
# [OUT]: The weather in Warsaw is currently:
# 	 - 23 degrees
# 	 - 60% humidity
# 	 - sunny


class Weather:
    def __init__(self, city, temp, humidity):
        self.city = city
        self.temp = temp
        self.humidity = humidity

    def report(self):
        return (
            f'The weather in {self.city} is currently:\n'
            f'\t - {self.temp} degrees\n\t - {self.humidity}% humidity'
        )


# Enter your solution here

class SunnyWeather(Weather):

    def __init__(self, uv_index, city, temp, humidity):
        super().__init__(city, temp, humidity)
        self.uv_index = uv_index

    def report(self):
        return (
            f'The weather in {self.city} is currently:\n'
            f'\t - {self.temp} degrees\n\t - {self.humidity}% humidity'
            f'\n\t - sunny'
        )


w = SunnyWeather('Warsaw', 23, 60, 80)
print(w.report())
