width = int(input("Enter a width of a rectangle: "))
assert width > 0, "The width value must be positive."
height = int(input("Enter a height of a rectangle: "))
assert height > 0, "The height value must be positive."

area = width * height
print(f"Area: {area}")