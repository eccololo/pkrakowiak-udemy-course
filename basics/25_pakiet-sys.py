from ast import arg
import sys

# Możemy wyprintować w konsoli nazwę pliku oraz parametry przekazane podczas 
# uruchamiania skryptu po spacji jak np. python pakiet-sys.py 10 15 45
print(sys.argv)

args = sys.argv
print("Nazwa pliku:", args.pop(0))

i = 1
while args:
    print("Argument nr. {}: {}".format(i, args.pop(0)))
    i += 1