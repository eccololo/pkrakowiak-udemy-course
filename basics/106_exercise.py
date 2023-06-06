# Załóżmy, że masz listę krotek, z których każda zawiera nazwę języka programowania i odpowiadające mu rozszerzenie pliku:
#
#
#
# languages = [
#     ('Python', '.py'),
#     ('JavaScript', '.js'),
#     ('C++', '.cpp'),
#     ('Java', '.java'),
# ]
#
#
# Potrzebujesz utworzyć nowy słownik, który odwzorowuje każde rozszerzenie pliku na odpowiadający mu język programowania. Otrzymany słownik wydrukuj do konsoli.
#
#
#
# Oczekiwany wynik:
#
#
#
# {'.py': 'Python', '.js': 'JavaScript', '.cpp': 'C++', '.java': 'Java'}


languages = [
    ('Python', '.py'),
    ('JavaScript', '.js'),
    ('C++', '.cpp'),
    ('Java', '.java'),
]

output = {tuple_item[1]: tuple_item[0] for tuple_item in languages}
print(output)