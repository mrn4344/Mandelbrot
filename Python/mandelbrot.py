import imaginary as im

class mandelbrot(object):
    """Class for making a generic mandelbrot point checker"""

    func = 0


    def power_func(self, power, z, c):
        """Generic power function for calculating mandelbrot
        arguments:
            power: integer = the power of z to use each iteration
            z    : imaginary
            c    : imaginary
        return z^power + c"""
        new_z = z.deepCopy()

        for i in range(1, power):
            new_z.mult(z)

        return new_z.add(c)


    def isInSet(self, c, n):
        """Calculates if a point c is in the set of the defined function
        arguments:
        c : imaginary
        n : integer
        return: if the point c, when iterated using the defined power function
        doesn't diverge after n itererations"""
        z = im.imaginary(0, 0)
        for i in range(0, n-1):
            z = self.power_func(self.func, z, c)

            if z.cMag() > 2:
                return False
        return True

    def __init__(self, func_power = 2):
        super(mandelbrot, self).__init__()
        self.func = func_power
