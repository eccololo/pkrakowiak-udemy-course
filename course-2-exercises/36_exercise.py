daily_energy = 6000
system_efficiency = 85
battery_capacity = 30000

# Enter your solution here
daily_efficiency = daily_energy * (system_efficiency / 100)
days_sustain = battery_capacity // daily_efficiency

print(f"The solar panel system output: {daily_efficiency} watt-hours/day.")
print(f"The battery can power the system for {int(days_sustain)} days.")