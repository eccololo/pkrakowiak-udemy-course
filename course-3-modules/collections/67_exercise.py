from collections import namedtuple


Student = namedtuple(
    typename='Student',
    field_names=['name', 'age', 'specialization'],
)

st1 = {
    'name': 'Kate',
    'age': 20,
    'specialization': 'mathematics'
}
st2 = {
    'name': 'Mike', 
    'age': 21, 
    'specialization': 'physics'
}
st3 = {
    'name': 'Bob',
    'age': 21,
    'specialization': 'information technology'
}

students_dicts = [st1, st2, st3]
students = []

for student in students_dicts:
    s = Student(student['name'], student['age'], student['specialization'])
    students.append(s)

for student in students:
    print(student)

