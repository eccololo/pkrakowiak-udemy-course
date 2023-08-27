courses = [
    'Introduction to Python',
    'Web Development',
    'Data Science',
    'Artificial Intelligence',
]
query = 'Big Data'

# Enter your solution here

for course in courses:
    if course == query:
        print(f"Course found: {query}")
        break
else:
    print("Course not found")