from string import Template


names = ['John', 'Paul', 'Lisa', 'Michael']

emails = Template("""Hello $name,
Thank you for visiting our website.
Team, XYZ""")

email_list = []

for name in names:
    email_list.append(emails.safe_substitute(name=name))

for email in email_list:
    print(email)
    print("-" * 35)
