with open("202_products.txt", "r") as f:
    data = f.readlines()


data = data[1:]
output = []
for item in data:
    item = item.replace("\n", "")
    output.append([item])

for item in output:
    print(item)