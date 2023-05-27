import re

message = 'For more information, please call: 123-456-789'

match_item = re.findall(pattern="[0-9]{1,3}-[0-9]{1,3}-[0-9]{1,3}", string=message)

print(match_item)