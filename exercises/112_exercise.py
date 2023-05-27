with open('plw_c.txt', 'r') as file:
    content = file.read().splitlines()

data_dict = {}
dates = []
closure = []
for idx, line in enumerate(content):
    if idx > 0:
        dates.append(line.split(",")[0])
        closure.append(float(line.split(",")[-2]))

data_dict["Data"] = dates
data_dict["Zamkniecie"] = closure

print(data_dict)