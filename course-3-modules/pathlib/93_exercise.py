from pathlib import Path


text = "Open,High,Low,Close"
path = Path.cwd() / 'hello_2.txt'

if not Path.is_file(path):
    with open(path, "w") as f:
        f.write(text)

with Path.open(path, "r") as f:
    content = f.read()

print(content)