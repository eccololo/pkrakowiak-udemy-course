import re

text = "Please send an email to info@template.com or call to: 123-456-789."

result = re.sub("\d{3}-\d{3}-\d{3}", "***-***-***", text)

print(result)