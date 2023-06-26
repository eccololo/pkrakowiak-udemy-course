import re

text = "Please send an email to info@template.com or sales-info@template.it"

match_list = re.findall(pattern="[a-zA-z-\.]+@[a-zA-Z]+\.[a-zA-Z]{2,5}", string=text)

print(match_list)