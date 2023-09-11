import numbers


values = [2.0, 2, '2.0', '2', None, False, True]

for item in values:
    if isinstance(item, numbers.Number):
        is_number = True
    else:
        is_number = False
    text = f"{item}   : {type(item)}    : {is_number}"
    print(text)