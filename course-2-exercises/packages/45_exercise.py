import re

text = """Python plays a key role in our production pipeline.
Without it a project the size of Star Wars: Episode II would have been very difficult to pull off."""

match_list = re.findall(pattern="[A-Z]{1,}[a-z]+", string=text)

print(match_list)