employee_id = 123451612
# Enter your solution here
username_number = employee_id % 10001
username_suffix = str(username_number)
username = "user_" + username_suffix

print(username)