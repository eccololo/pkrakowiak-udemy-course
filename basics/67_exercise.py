hour = 8
solar_power = 50
battery_capacity = 500
battery_level = 0

# Enter your solution here

while battery_level <= battery_capacity and hour < 15:
    battery_level += solar_power
    hour += 1

print(f"The solar battery charge level is: {battery_level} Watt-hours.")