from collections import namedtuple


Student = namedtuple(
    typename='Student',
    field_names=['name', 'age', 'specialization'],
)

data_file_path = "course-3-modules/collections/students.txt"

with open(data_file_path, "r") as file:
    students_dicts = [line.rstrip() for line in file]

students = []

for student in students_dicts:
    student = eval(student)
    s = Student(student['name'], student['age'], student['specialization'])
    students.append(s)

print(students)