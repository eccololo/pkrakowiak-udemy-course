# [IN]: os.listdir(".")

# [OUT]:
# exercise.py
# evaluate.py
# result.py
# run_unittest.py

import os

dir_list = os.listdir(".")
for item in dir_list:
    if item.endswith(".py"):
        print(item)