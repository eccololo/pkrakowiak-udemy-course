from pathlib import Path

path = Path.cwd() / "104_README.md"

with path.open(mode="r", encoding="utf-8") as md_file:
    content = md_file.readlines()
    for line in content:
        line = line.replace("\n", "")
        if line.startswith("#"):
            print(line)