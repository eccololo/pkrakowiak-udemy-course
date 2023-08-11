users = [
    {'name': 'Alice', 'age': 25, 'email': 'alice@EXAMPLE.com'},
    {'name': 'Bob', 'age': '35', 'email': 'bob@example.com'},
    {'name': 'Charlie', 'age': 45.0, 'email': 'CHARLIE@example.com'},
]


def process_user(user):
    # Enter your solution here
    age = user["age"]
    age = int(age)
    user["age"] = age

    email = user['email']
    email = email.lower()
    user['email'] = email

    return user


processed_users = list(map(process_user, users))
for user in processed_users:
    print(user)