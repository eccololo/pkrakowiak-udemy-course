sunlight_intensity = 500.0

# Enter your solution here

output_power = None

if sunlight_intensity <= 200:
    output_power = 0
elif 200 < sunlight_intensity <= 400:
    output_power = 100
elif 400 < sunlight_intensity <= 600:
    output_power = 200
else:
    output_power = 300

print(f"Power output of the solar panel is {output_power} watts.")