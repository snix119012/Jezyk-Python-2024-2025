import math
from math import hypot, atan2, sin, cos


class Zespolona:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def conjugate(self):
        return self.__class__(self.r, -self.i)

    def argz(self):
        return atan2(self.i, self.r)

    def __abs__(self):
        return math.sqrt((self.r * self.r) + (self.i * self.i))

    def __repr__(self):
        return f"Zespolona({self.r}, {self.i})"

    def __str__(self):
        return f"({self.r}{'+' if self.i >= 0 else ''}{self.i}j)"

    def __add__(self, other):
        if isinstance(other, Zespolona):
            return Zespolona(self.r + other.r, self.i + other.i)
        elif isinstance(other, (int, float)):
            return Zespolona(self.r + other, self.i)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other,Zespolona):
            return Zespolona((self.r - other.r) , (self.i - other.i))
        else:
            return Zespolona((self.r - other) ,self.i)


    def __mul__(self, other):
        if isinstance(other,Zespolona):
            return Zespolona((self.r * other.r - self.i * other.i) , (self.r * other.i + self.i * other.r))
        else:
            return Zespolona(self.r * other, self.i * other)
    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return Zespolona(other - self.r, -self.i)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        if isinstance(other, Zespolona):
            if self.r == other.r and self.i == other.i:
                return True
            else:
                return False

    def __ne__(self, other):
        if isinstance(other,Zespolona):
            if self.r != other.r or self.i != other.i:
                return True
            else:
                return False
        return False
    def __pow__(self, other):
        if isinstance(other, int):
            if other == 0:
                return Zespolona(1, 0)
            result = self
            for _ in range(abs(other) - 1):
                result *= self
            if other < 0:
                return Zespolona(1, 0) / result
            return result
        return False

    def __truediv__(self, other):
        if isinstance(other, Zespolona):
                return Zespolona((self.r * other.r + self.i * other.i) /  (other.r ** 2 + other.i ** 2), (self.i * other.r - self.r * other.i) /  ((other.r ** 2) + (other.i ** 2)))
        elif isinstance(other, (int, float)):
                return Zespolona(self.r / other, self.i / other)
        return False

def main():
    print("Liczby zespolone")
    a = Zespolona(2, 5)
    b = Zespolona(1, -3)
    print(a)
    print(b)
    b_copy = eval(repr(b))
    print(type(b_copy), b_copy.r, b_copy.i)
    print(a + b)
    print(a - b)
    print(a + 4)
    print(7 - a)
    print(a * 4)
    print(a * (-4))
    print(a == Zespolona(2, 5))
    print(a == b)
    print(a != b)
    print(a != Zespolona(2, 5))
    print(a ** 2)
    print(b ** 4)
    print(a / b)


if __name__ == "__main__":
    main()

# Liczby zespolone
# (2+5j)
# (1-3j)
# <class '__main__.Zespolona'> 1 -3
# (3+2j)
# (1+8j)
# (6+5j)
# (5-5j)
# (8+20j)
# (-8-20j)
# True
# False
# True
# False
# (-21+20j)
# (28+96j)
# (-1.3+1.1j)
