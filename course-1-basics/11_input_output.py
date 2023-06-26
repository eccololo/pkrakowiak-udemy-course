# file = open("simple.txt", "r")
#
# for line in file:
#     print(line, end="")
#
# file.close()

# with open("simple.txt", "r") as file:
#     for line in file:
#         print("Linia:", line, end="")
#
# with open("simple.txt", "r") as file:
#     line = file.readline()
#     print(line)

# with open("simple.txt", "r") as file:
#     line = file.readlines()
#     print(line)
#
# Writing to a file.

# techs = ["Java", "Ruby", "Python", "PHP", "jQuery"]
# with open("techs.txt", "w") as file:
#     for tech in techs:
#         print(tech, file=file)
#
# even_numbers = list(range(100))[::2]
# with open("even.txt", "w") as file:
#     for number in even_numbers:
#         file.write(str(number) + "\n")

# techs = ["Java", "Ruby", "Python", "PHP", "jQuery"]
# with open("techs.txt", "a") as file:
#     for tech in techs:
#         print(tech, file=file)

#spaces = 10
# stars = 1
# with open("tree.txt", "w") as file:
#     for i in range(11):
#         file.write(" " * (spaces - i) + "*" * (stars + i) + " " * (spaces - i) + "\n")

with open("tree.txt", "w") as file:
    for j in range(2):
        for i in range(10):
            print("{:>9}".format("*" * i), end="", file=file)
            print("{}".format("*" * i), file=file)
