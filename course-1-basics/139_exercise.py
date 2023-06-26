# [IN]: r1 = Rectangle(4, 5)
# [IN]: r1
#
# [OUT]: Rectangle(4, 5)
#
# [IN]: r1 = Rectangle(4, 5)
# [IN]: print(r1)
#
# [OUT]: Rectangle(4, 5)


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Enter your solution here

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __str__(self):
        return f"Rectangle({self.width}, {self.height})"


r1 = Rectangle(4, 5)
print(r1)
#
# [OUT]: Rectangle(4, 5)
