from pathlib import Path

# path = Path(Path.cwd() / 'reports/ecommerce/2020/01')
# path_parts = path.parts
# for idx, item in enumerate(path_parts):
#     path_item = Path(Path.cwd() / item)
#     if idx == 0:
#         continue
#     if not Path.is_dir(path_item):
#         Path.mkdir(path_item)
#
# for idx, item in enumerate(path_parts):
#     path_item = Path(Path.cwd() / item)
#     if Path.is_dir(path_item):
#         print(True)

# Other solution

path = Path.cwd() / 'reports/ecommerce/2020/01'
path.mkdir(parents=True)
print(path.is_dir())