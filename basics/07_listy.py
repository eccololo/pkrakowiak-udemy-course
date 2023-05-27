empty_list = list()
print(empty_list)

languages = ["java", "css", "python", "html"]
print(languages[0])
languages[2] = "Python 3.7"
print(languages[2])

languages += ["Ruby"]
print(languages)

techs = []
techs.append("python")
techs.append("java")
techs.append(["hadpoop", "r"])
techs.extend(["sql", "sass"])
techs.insert(0, "go")
techs.insert(3, "ruby")
print(techs)

# removes last element from list.
techs.pop()
print(techs)

techs = ["sql", "python", "java"]
# removes element at specifics index number.
techs.pop(0)
print(techs)

techs = ["sql", "python", "java"]
print(techs.index("java"))
# print(techs.index("abc"))

techs = ["sql", "python", "java", "html", "css"]

# Sorting list
# techs.sort()
# techs.sort(reverse=True)
print(techs)

# print(techs[::-1])
techs.reverse()
print(techs)