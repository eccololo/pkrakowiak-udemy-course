import string


docs = 'programming in python'

ascii_chars = string.ascii_lowercase

code_map = {k:v for k,v in enumerate(ascii_chars)}
code_map_inv = {v:k for k,v in enumerate(ascii_chars)}

output = ""
for char_x in docs:
    if char_x != " ":
        idx = code_map_inv[char_x]
        idx += 3
        if idx > 25:
            idx %= 26
        output += code_map[idx]
    else:
        output += " "

print(output)