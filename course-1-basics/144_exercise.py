# [IN]: z1 = ComplexNumber(2, 3)
# [IN]: z2 = ComplexNumber(-1, 2)
# [IN]: z1 + z2
# [OUT]: ComplexNumber(1, 5)
#
#
# [IN]: z1 = ComplexNumber(2, 3)
# [IN]: z2 = ComplexNumber(-1, 2)
# [IN]: z1 - z2
# [OUT]: ComplexNumber(3, 1)


class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag < 0:
            return f'{self.real} - {-self.imag}i'
        else:
            return f'{self.real} + {self.imag}i'

    # Enter your solution here

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)


z1 = ComplexNumber(2, 3)
z2 = ComplexNumber(-1, 2)
print(z1 + z2)
# [OUT]: ComplexNumber(1, 5)
#
#
z1 = ComplexNumber(2, 3)
z2 = ComplexNumber(-1, 2)
print(z1 - z2)
# [OUT]: ComplexNumber(3, 1)
