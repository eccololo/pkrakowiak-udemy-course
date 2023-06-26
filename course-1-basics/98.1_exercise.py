# [IN]: [
#     'run_me.py',
#     'README.md',
#     'help.txt.',
#     'script.py',
#     'menu.py',
#     'main.py',
#     'py',
# ]

# [OUT]: generator py_file_generator()

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