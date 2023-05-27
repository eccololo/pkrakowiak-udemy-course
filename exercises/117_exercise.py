import csv

headers = ['user_id', 'amount']
users = [['001', '1400'], ['004', '1300'], ['007', '900']]

with open("users.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    for user in users:
        writer.writerow(user)

