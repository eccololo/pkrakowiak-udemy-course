employees = [
    {'name': 'John', 'salary': 60000},
    {'name': 'Jane', 'salary': 55000},
    {'name': 'Bob', 'salary': 40000},
    {'name': 'Sara', 'salary': 70000},
    {'name': 'Mike', 'salary': 52000},
]
min_salary = 55000

# Enter your solution here

for employee in employees:
    if employee['salary'] >= 55000:
        print(f"{employee['name']} has a salary of ${employee['salary']}")
    if employee['salary'] < min_salary:
        print(f"STOP! {employee['name']} with ${employee['salary']}")
        break