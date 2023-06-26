with open("playway.txt") as f:
    lines = f.read().splitlines()

data = []
for idx, line in enumerate(lines):
    if idx > 0:
        data.append(int(line.split(",")[-2]))

data_avg = sum(data) / len(data)

print("3-dniowa średnia cena zamknięcia: {:.2f}".format(data_avg))