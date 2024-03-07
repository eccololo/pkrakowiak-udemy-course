import re

code = 'PL code: XG-GH-110'

output = re.findall('(PL).+(110)', code)

all = []
all.append(output[0][0])
all.append(output[0][1])
print(all)

# Better solution

output = re.findall('PL|\d+', code)
print(output)