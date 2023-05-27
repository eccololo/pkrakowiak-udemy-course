import re
password = 'my_password_123'

# Enter your solution here
if not len(password) >= 8:
    print('The password is too short.')
elif re.search("[0-9]", password) is None:
    print('The password must contain at least one digit.')
elif re.search("[A-Z]", password) is None:
    print('The password must contain at least one uppercase letter.')
else:
    print('The password is complex enough.')