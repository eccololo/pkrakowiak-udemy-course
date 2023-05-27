fruits = {'apple': 2, 'banana': 3}
# Enter your solution here

print("Dictionary before update:", fruits)
fruits["apple"] = 4
print("Dictionary after update:", fruits)
fruits["kiwi"] = 1
print("Dictionary after adding:", fruits)
dict2 = {"orange": 3, "peach": 2}
fruits.update(dict2)
print("Dictionary after merging:", fruits)
