import string

code_map = {key: value for key, value in enumerate(string.ascii_lowercase)}
code_map_inv = {value: key for key, value in code_map.items()}

print(code_map)
print(code_map_inv)

docs = 'programming in python'


def encode(tekst, shift=3):
    output_tekst = ""
    for x in tekst:
        if x == " ":
            output_tekst += " "
            continue
        idx = code_map_inv[x]
        idx += shift
        if idx > 25:
            idx %= 25
            idx -= 1
        output_tekst += code_map[idx]
    return output_tekst


print(encode(docs))
