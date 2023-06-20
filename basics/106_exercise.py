# [IN]: [
#     ('Python', '.py'),
#     ('JavaScript', '.js'),
#     ('C++', '.cpp'),
#     ('Java', '.java'),
# ]

# [OUT]: {'.py': 'Python', '.js': 'JavaScript', '.cpp': 'C++', '.java': 'Java'}


languages = [
    ('Python', '.py'),
    ('JavaScript', '.js'),
    ('C++', '.cpp'),
    ('Java', '.java'),
]

output = {tuple_item[1]: tuple_item[0] for tuple_item in languages}
print(output)