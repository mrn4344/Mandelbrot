class imaginary(object):
    """Class for representing, and doing arithmatic with complex numbers"""

    re = 0
    im = 0

    @staticmethod
    def cAdd(a, b):
        """Method for computing complex addition.
        Arguments:
             a & b: imaginary objects
        Return: A new imaginary with the value of a + b
        Note: All reference other than returned remain unchanged"""
        return imaginary(a.re + b.re, a.im + b.im)


    @staticmethod
    def cMult(a, b):
        """Method for computing complex multiplicationself.
        Arguments:
            self & c: imaginary objects
        Return: A new imaginary with the value of a * b
        Note: All reference other than returned remain unchanged"""
        return imaginary( (a.re * b.re) - ( a.im * b.im) , ( (a.re * b.im) + (a.im * b.re) ) )


    def add(c):
        """Method for computing complex addition.
        Arguments:
             self & c: imaginary objects
        Return: Self with the updated value of self + c.
        Note: Changes value of self"""
        self.re = self.re + c.re
        self.im = self.im + c.im
        return self


    def mult(c):
        """Method for computing complex multiplicationself.
        Arguments:
            self & c: imaginary objects
        Return: Self with the updated value of self * c.
        Note: Changes value of self"""
        self.re = (self.re * c.re) - ( self.im * c.im)
        self.im = (self.re * c.im) + (self.im * c.re)
        return self


    def __init__(self, real, complex):
        super(imaginary, self).__init__()
        self.re = real
        self.im = complex
