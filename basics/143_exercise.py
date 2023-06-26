# [IN]: z = ComplexNumber(1, 2)
# [IN]: print(z)
# [OUT]: 1 + 2i
#
#
# [IN]: z = ComplexNumber(-1, 2)
# [IN]: print(z)
# [OUT]: -1 + 2i
#
#
# [IN]: z = ComplexNumber(-1, -2)
# [IN]: print(z)
# [OUT]: -1 - 2i

class ComplexNumber:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag < 0:
            return f'{self.real} - {abs(self.imag)}i'
        else:
            return f'{self.real} + {abs(self.imag)}i'


z = ComplexNumber(-1, -2)
print(z)
# [OUT]: -1 - 2i
