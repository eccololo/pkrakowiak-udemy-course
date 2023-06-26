url = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'

last_char = url.rfind("/") + 1
last_part = url[last_char:]
output = last_part.replace("-", " ")
print(output)