# {'name': 'smartfon', 'price': 3000.0, 'quantity': 10}
# {'name': 'laptop', 'price': 5000.0, 'quantity': 5}
# {'name': 'tablet', 'price': 2000.0, 'quantity': 12}

with open("71_products.txt" , "r") as f:
    data = f.readlines()

output = []
for item in data:
    temp_dict = {}
    row = item.strip().split(",")
    temp_dict["name"] = row[0]
    temp_dict["price"] = float(row[1])
    temp_dict["quantity"] = row[2]
    output.append(temp_dict)

for x_dict in output:
    print(x_dict)
