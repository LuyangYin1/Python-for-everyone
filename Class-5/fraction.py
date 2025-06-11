class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __truediv__(self, other):  # Overloading the / operator
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __add__(self, other):  # Overloading the / operator
        new_numerator2 = self.numerator + other.numerator
        new_denominator2 = self.denominator + other.denominator
        return Fraction(new_numerator2, new_denominator2)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"