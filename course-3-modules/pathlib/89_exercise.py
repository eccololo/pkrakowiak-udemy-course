from pathlib import Path

path_cwd = Path.cwd()
reports_path = path_cwd / 'reports'

if not Path.is_dir(reports_path):
    Path.mkdir(reports_path)

for item in sorted(Path.iterdir(path_cwd)):
    print(item)