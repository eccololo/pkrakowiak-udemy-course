text = "Witaj na kursie Pythona.\nPython to wspanialy jezyk"

print(dir(text))

# help zwraca nam informację o metodzie którą przekazalismy do tej metody
print(help(str.count))

print(text.capitalize())
print(text.title())
print(text.count("Python"))
print(text.startswith("Wi"))
print(text.endswith("zyk"))

"some_script.py".endswith(".py")

print("sample.png".endswith(".png"))

print(text.find("Python"))
print(text[text.find("Python"):])

print("mateusz1234 ".isalnum())

print("12345mat".isdigit())

print("MATEUsZ".isupper())
print("mateusZ".islower())

print(" ".join(["Python", "3.7"]))
print("#".join(["sport", "fit", "gym"]))
print(",".join(["1", "2", "3", "4"]))

print("column name".replace(" ", "_"))

print("    python    ".strip())
print("    python    ".rstrip())
print("    python    ".lstrip())

print("1,2,3,4,5,6".split(","))
print("java python css html bootstrap".split())


print("12".zfill(5))
print("1".zfill(10))