with open('plw_d.txt', 'r') as file:
    content = file.read().splitlines()

max = 0
dzien = None
for idx, item in enumerate(content):
    if idx > 0:
        item_list = item.split(",")
        wolumen = int(item_list[-1])
        print(wolumen)
        if wolumen > max:
            max = wolumen
            dzien = item_list[0]

print(f"Data: {dzien}")