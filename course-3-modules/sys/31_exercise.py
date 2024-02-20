import sys

saved_stdout = sys.stdout
with open("logs.txt", "w") as sys.stdout:
    print('Logging...')
    print('Connecting...')
    print('Closing...')

sys.stdout = saved_stdout
print('Completed successfully')