with open("203_data.csv", "r") as f:
    data = f.readlines()

output = []
for idx, item in enumerate(data):
    if idx == 0:
        continue
    power = item.split(",")[2]
    power = power.replace("\n", "")
    output.append(float(power))
print(f"Average energy generated: {round(sum(output) / len(output), 2)} kWh")