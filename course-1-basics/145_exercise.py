# [IN]: z1 = ComplexNumber(1, 1)
# [IN]: z2 = ComplexNumber(-1, 2)
# [IN]: z1 + z2
# [OUT]: ComplexNumber(-3, 1)
#
#
# [IN]: z1 = ComplexNumber(2, 3)
# [IN]: z2 = ComplexNumber(2, 3)
# [IN]: z1 == z2
# [OUT]: True
#
#
# [IN]: z1 = ComplexNumber(2, 3)
# [IN]: z2 = ComplexNumber(2, 1)
# [IN]: z1 == z2
# [OUT]: False

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag < 0:
            return f'{self.real} - {-self.imag}i'
        else:
            return f'{self.real} + {self.imag}i'

    def __add__(self, other):
        new_real = self.real + other.real
        new_imag = self.imag + other.imag
        return ComplexNumber(new_real, new_imag)

    def __sub__(self, other):
        new_real = self.real - other.real
        new_imag = self.imag - other.imag
        return ComplexNumber(new_real, new_imag)

    # Enter your solution here

    def __mul__(self, other):
        real_num = self.real * other.real + (self.imag * other.imag * -1)
        imag_num = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_num, imag_num)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag


z1 = ComplexNumber(2, 3)
z2 = ComplexNumber(2, 1)
print(z1 == z2)
# [OUT]: False
