import re

code = '0010-000-423-22'


output = re.findall('\d{2,4}', code)

print(output)