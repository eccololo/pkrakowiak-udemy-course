from collections import namedtuple


Student = namedtuple(
    typename='Student',
    field_names=['name', 'age', 'specialization'],
)

st1 = {
    'name': 'Kate',
    'age': 20,
    'specialization': 'mathematics',
}
st2 = {
    'name': 'Mike',
    'age': 21,
    'specialization': 'physics'
}
st3 = {
    'name': 'Bob',
    'age': 21,
    'specialization': 'information technology',
}

mike = Student(st1["name"], st1["age"], st1["specialization"])
kate = Student(st2["name"], st2["age"], st2["specialization"])
bob = Student(st3["name"], st3["age"], st3["specialization"])

students = []
students.append(mike)
students.append(kate)
students.append(bob)

for student in students:
    print(student)