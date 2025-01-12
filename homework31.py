# 1․ Գրել Calculator class, որը․
#    - __init__ ում կստանա թիվ և կստուգի այդ թվի int կամ float լինելը, հակառակ դեպքում կվերադարձնի Error,
#    - կունենա միայն getter մեթոդ տրված թիվը ստանալու համար, իսկ այդ թիվը կլինի private,
#    - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (+, -, *, /, //, %, **),
#    - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (+=, -=, *=, /=, //=, %=, **=),
#    - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (==, >, >=, <, <=, !=),
#    - վերոնշյալ մեթոդները ռեալիզացված կլինեն այնպես, որ աշխատեն նաև Calculator կլասի երկու օբյեկտների համար,
#    - կունենա համապատասխան magic մեթոդներ, որոնք թույլ կտան օբյեկտը տպելուց․ ստանալ թիվը (__str__), ստանալ թիվը և թվի տիպը (__repr__)։


class Calculator:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, n):
        if type(n) == int or type(n) == float:
            self.__n  = n
        else:
            raise ValueError('wrong number')

    @property
    def n(self):
        return self.__n

    def __str__(self):
        return f"{self.__n}"

    def __repr__(self):
        return f"{type(self.n)}"

    def __add__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__n + other.__n)
        else:
            return Calculator(self.__n + other)
    def __sub__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__n - other.__n)
        else:
            return Calculator(self.__n - other)
    def __mul__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__n * other.__n)
        else:
            return Calculator(self.__n * other)
    def __truediv__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__n / other.__n)
        else:
            return Calculator(self.__n / other)
    def __floordiv__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__n // other.__n)
        else:
            return Calculator(self.__n // other)
    def __mod__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__n % other.__n)
        else:
            return Calculator(self.__n % other)
    def __pow__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__n ** other.__n)
        else:
            return Calculator(self.__n ** other)
    def __iadd__(self, other):
        if isinstance(other, Calculator):
            self.__n += other.__n
        return self.__n
    def __isub__(self, other):
        if isinstance(other, Calculator):
            self.__n -= other.__n
        return self.__n
    def __imul__(self, other):
        if isinstance(other, Calculator):
            self.__n *= other.__n
        return self.__n
    def __itruediv__(self, other):
        if isinstance(other, Calculator):
            self.__n /= other.__n
        return self.__n
    def __ifloordiv__(self, other):
        if isinstance(other, Calculator):
            self.__n //= other.__n
        return self.__n
    def __imod__(self, other):
        if isinstance(other, Calculator):
            self.__n %= other.__n
        return self.__n
    def __ipow__(self, other):
        if isinstance(other, Calculator):
            self.__n **= other.__n
        return self.__n

    def __eq__(self, other):
        if isinstance(other, Calculator):
            other = other.__n
        return self.__n == other
    def __ne__(self, other):
        if isinstance(other, Calculator):
            other = other.__n
        return self.__n != other
    def __lt__(self, other):
        if isinstance(other, Calculator):
            other = other.__n
        return self.__n < other
    def __gt__(self, other):
        if isinstance(other, Calculator):
            other = other.__n
        return self.__n > other
    def __le__(self, other):
        if isinstance(other, Calculator):
            other = other.__n
        return self.__n <= other
    def __ge__(self, other):
        if isinstance(other, Calculator):
            other = other.__n
        return self.__n >= other

a = Calculator(6)
b = Calculator(3)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
