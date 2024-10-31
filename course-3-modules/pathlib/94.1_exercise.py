from pathlib import Path


path = Path.cwd() / 'hello.txt'

path.write_text("Open,High,Low,Close")
print(path.read_text())