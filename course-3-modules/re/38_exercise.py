import re

text = 'Python 3.10'

output = re.findall('\D', text)

print(output)

