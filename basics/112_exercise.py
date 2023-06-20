# [IN]:  [
#     {
#         'id': 1,
#         'name': 'Python for Beginners',
#         'tags': ['Python', 'Programming', 'Beginner']
#     },
#     {
#         'id': 2,
#         'name': 'Data Science with Python',
#         'tags': ['Python', 'Data Science', 'Statistics']
#     },
#     {
#         'id': 3,
#         'name': 'Machine Learning',
#         'tags': ['Python', 'Machine Learning']
#     }
# ]

# [OUT]:  {
#     'Data Science',
#     'Programming',
#     'Python',
#     'Machine Learning',
#     'Beginner',
#     'Statistics',
# }

courses = [
    {
        'id': 1,
        'name': 'Python for Beginners',
        'tags': ['Python', 'Programming', 'Beginner']
    },
    {
        'id': 2,
        'name': 'Data Science with Python',
        'tags': ['Python', 'Data Science', 'Statistics']
    },
    {
        'id': 3,
        'name': 'Machine Learning',
        'tags': ['Python', 'Machine Learning']
    }
]

# Enter your solution here

unique_tags = {tag for course in courses for tag in course['tags']}

print(unique_tags)