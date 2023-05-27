# ['Printed T-shirt', '29.99', 'Classic white t-shirt with a printed design on the front']
# ['Sweatpants', '49.99', 'Black sweatpants made from a soft material']
# ['Evening Dress', '99.99', 'Elegant evening dress with a deep neckline']
# ['Sport Shoes', '79.99', 'Lightweight sport shoes perfect for running.']

output = []
with open("70_products.txt", "r") as f:
    for idx, line in enumerate(f):
        if idx == 0:
            continue
        output.append(line.strip().split(";"))

for item in output:
    print(item)
