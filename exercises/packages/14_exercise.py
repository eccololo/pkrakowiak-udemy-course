import os

cwd_split = os.getcwd().split("\\")
working_dir = cwd_split[len(cwd_split) - 1]
print(working_dir)