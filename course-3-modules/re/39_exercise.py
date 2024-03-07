import re

code = '0010-000-423'

output = re.findall('[1-9]', code)

print(output)