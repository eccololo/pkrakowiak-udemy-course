import sys

# Open a file for writing
with open('181_output.txt', 'w') as file:
    # Use sys.stdout to redirect the standard output to a file
    sys.stdout = file

    # Print some output
    print('This output will be written to a file')

# The standard output is now back to the console
print('This output will be printed to the console')