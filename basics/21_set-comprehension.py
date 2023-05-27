mytext = "Python jest wspanialy. Python jest elastyczny. Python rzadzi."
words = mytext.lower().replace(".", "").split()
print(words)

unique_words = {word for word in words}
print(unique_words)
print(type(unique_words))

unique_words_gt_4 = {word for word in words if len(word) > 4}
print(unique_words_gt_4)

unique_words_capitalize = {word.capitalize() if word.startswith("pyt") else word for word in words}
print(unique_words_capitalize)