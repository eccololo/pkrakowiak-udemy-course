import re


message = 'For more information, please call: 123-456-789'
result = re.findall("\d{3}-\d{3}-\d{3}", message)

print(result[0])

