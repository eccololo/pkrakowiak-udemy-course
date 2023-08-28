with open("196.1_data.txt", "r") as f:
    data = f.readlines()

for item in data:
    item = item.replace("\n", "")
    print(item)