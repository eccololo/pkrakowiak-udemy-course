from pathlib import Path

path = Path.cwd() / 'reports/ecommerce/2020/01'

if not path.is_dir():
    path.mkdir(parents=True)
    print("Success!")