from pathlib import Path
import re


pattern = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"

path = Path.cwd() / "105_README.md"

with path.open(mode="r", encoding="utf-8") as md_file:
    content = md_file.read()
    found_links = re.findall(pattern, content)
    found_links = set(found_links)
    for link in sorted(found_links):
        print(link)