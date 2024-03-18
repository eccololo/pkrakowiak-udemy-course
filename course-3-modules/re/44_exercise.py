import re


text = "Please send an email to info@template.com or sales-info@template.it"

result = re.findall("[a-zA-Z]+@[a-zA-Z]+.[a-z]{2,3}", text)

print(result)