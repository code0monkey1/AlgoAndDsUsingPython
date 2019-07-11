import  math
class Fraction():
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator


    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):

        num=self.numerator*other.denominator+self.denominator*other.numerator
        den=self.denominator*other.denominator

        __gcd= math.gcd(num,den)
        print(f"the GCD is {__gcd}")
        num/=__gcd
        den/=__gcd

        return Fraction(num,den)

    def __gt__(self, other):
        return self.numerator*other.denominator>other.numerator*self.denominator

    def __eq__(self, other):
        return self.numerator*other.denominator==other.numerator*self.denominator

my_fraction = Fraction(2,5)
print(my_fraction)
my_other_fraction=Fraction(3,4)
print(my_other_fraction)

print(my_fraction+my_other_fraction)
print(f" the first fraction is {my_fraction} while the second fraction is {my_other_fraction}")
print(my_fraction>my_other_fraction)

print( my_fraction == Fraction(2,5))