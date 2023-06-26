with open('plw_d.txt', 'r') as file:
    content = file.read().splitlines()

max = 0
for idx, line in enumerate(content):
    if idx > 0:
        wolumen = int(line.split(",")[-1])
        if wolumen > max:
            max = wolumen

print("Max Vol: {}".format(max))