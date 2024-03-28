from collections import namedtuple


Student = namedtuple(
    typename='Student',
    field_names=['name', 'age', 'specialization'],
)

students = [
    Student('Mike', 21, 'physics'),
    Student('Mark', 22, 'biology'),
    Student('Kate', 20, 'mathematics'),
    Student('Bob', 21, 'information technology'),
]

students = sorted(students, key=lambda x: x.age)
print(students)