# Dana jest lista zawierająca nazwy plików w pewnym katalogu:
#
#
#
# files = [
#     'run_me.py',
#     'README.md',
#     'help.txt.',
#     'script.py',
#     'menu.py',
#     'main.py',
#     'py',
# ]
#
#
# Stwórz generator o nazwie py_file_generator(), który przefiltruje podane nazwy i będzie zwracał tylko nazwy plików z rozszerzeniem '.py'.
#
#
#
# Uwaga: Aby zaliczyć ćwiczenie wystarczy zdefiniować generator. Nie trzeba go wywoływać. Zaimplementowane testy sprawdzają poprawność działania generatora.

def py_file_generator(list_of_files):
    for item in list_of_files:
        if item.endswith(".py"):
            yield item


files = [
    'run_me.py',
    'README.md',
    'help.txt.',
    'script.py',
    'menu.py',
    'main.py',
    'py',
]

print(py_file_generator(files))