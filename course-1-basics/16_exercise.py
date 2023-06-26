string = 'Programowanie w języku Python - od A do Z'
string = string.lower()
string = string.replace("-", "").replace(" ", "")
string = string.replace("ą", "a").replace("ć", "c")

print(len(set(string)))