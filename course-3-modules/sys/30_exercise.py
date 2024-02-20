import sys

output_list = []
for i, arg in enumerate(sys.argv):
    if i == 0:
        continue

    output_list.append(int(arg))

if len(output_list) > 0:
    output = sum(output_list) / len(output_list)
    print(output)
else:
    print('No values were given.')