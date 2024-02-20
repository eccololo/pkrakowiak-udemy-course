import os

names = [item for item in os.listdir(os.getcwd()) if item.startswith("16")]

print(sorted(names))