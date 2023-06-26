# [IN]: os.getcwd()

# [OUT]:
# exercise.py
# evaluate.py
# __pycache__
# result.py
# run_unittest.py

import os

dir_list = os.listdir(os.getcwd())
for item in dir_list:
    print(item)