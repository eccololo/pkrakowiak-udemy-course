from collections import namedtuple
import json

Student = namedtuple(
    typename='Student',
    field_names=['name', 'age', 'specialization'],
)

with open("students.txt", "r") as f:
    data = f.read()
    data = data.replace("'", "\"")

students_attrs = data.split("\n")
student_attrs_list = []
for attrs in students_attrs:
    student_attrs_list.append(json.loads(attrs))

students = [Student(**student_attrs_list[0]), Student(**student_attrs_list[1]), Student(**student_attrs_list[2])]
print(students)