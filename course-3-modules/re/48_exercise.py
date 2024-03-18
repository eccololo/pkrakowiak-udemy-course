import re


text = "Please send an email to info@template.com or call to: 123-456-789."
phone_number = re.findall("\d{3}-\d{3}-\d{3}", text)
text = text.replace(phone_number[0], "***-***-***")
print(text)