from pathlib import Path


path = Path.cwd() / 'hello.txt'

if not path.is_file():
    with open(path, "w") as f:
        f.write("Open,High,Low,Close")

with open(path, "r") as f:
    print(f.read())