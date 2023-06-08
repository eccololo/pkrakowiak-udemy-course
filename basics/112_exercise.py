# Załóżmy, że pracujesz nad projektem platformy e-learningowej, która ma bazę kursów i chcesz znaleźć wszystkie unikalne tagi, które są powiązane z kursami. Masz listę słowników, gdzie każdy słownik reprezentuje kurs, a klucz 'tags' w każdym słowniku zawiera listę tagów powiązanych z kursem:
#
#
#
# courses = [
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
#
#
# Potrzebujesz znaleźć wszystkie unikalne tagi, które są powiązane z kursami. Przypisz je do zmiennej o nazwie unique_tags.
#
#
#
# Oczekiwana postać zbioru unique_tags (widok sformatowany dla lepszego wyświetlenia):
#
#
#
# {
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