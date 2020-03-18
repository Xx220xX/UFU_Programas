class Polinomio:
    def __init__(self, *p):
        if len(p) > 0:
            if isinstance(p[0], list):
                p = p[0]
            elif isinstance(p[0], str):
                p = []

        self.coef = list(reversed(p))

    def show(self):
        print(self.coef)

    def len(self):
        return len(self.coef)

    def __repr__(self):
        st = ""
        i = len(self.coef) - 1
        while i >= 0:
            if abs(self.coef[i]) != 0:
                if self.coef[i] < 0:
                    st += f" - "
                elif st != "":
                    st += f" + "
                if abs(self.coef[i]) != 1 or i == 0:
                    st += f'{abs(self.coef[i])}'
                if i > 0:
                    st += ' x'
                if i > 1:
                    st += f'^{i}'
            i -= 1
        if st == "":
            return "0"
        return st

    def simplify(self):
        i = self.len()
        while i >= 0:
            if self[i] != 0:
                break
            i -= 1
        self.coef = self.coef[0:1 + i]

    def __getitem__(self, i):
        if i >= 0 and i < len(self.coef):
            return self.coef[i]
        return 0

    def __add__(self, other):
        ans = Polinomio()
        i = 0
        while i < self.len() or i < other.len():
            ans.coef.append(self[i] + other[i])
            i += 1
        ans.simplify()
        return ans

    def __sub__(self, other):
        ans = Polinomio()

        i = 0
        while i < self.len() or i < other.len():
            ans.coef.append(self[i] - other[i])
            i += 1
        ans.simplify()
        return ans

    def __mul__(self, other):
        ans = Polinomio()
        if isinstance(other, (int, float,)):
            other = Polinomio(other)
        for i in range(self.len() + other.len()):
            ans.coef.append(0)
        i = 0
        while i < self.len():
            j = 0
            while j < other.len():
                ans.coef[i + j] = ans.coef[i + j] + self[i] * other[j]
                j += 1
            i += 1
        ans.simplify()
        return ans

    def copy(self):
        ans = Polinomio(list(reversed(self.coef)))
        return ans

    def __truediv__(self, other):
        return self // other

    def __mod__(self, other):
        return self - self // other * other

    def __floordiv__(self, other):
        """
        pegar o termo de maior grau (polinomio.len()-1)
        dividir pelo polinomio de maior grau do segundo
        expoente se subtrai , e divide p/q
        """

        ans = Polinomio()
        div = self.copy()  # polinomio a dividir
        den = other.copy()  # polinomio que divide
        ans.coef = [0] * div.len()
        i = div.len() - 1
        j = den.len() - 1

        while i - j >= 0:
            termo = div[i] / den[j]
            sub = Polinomio([0] * (i - j + 1))
            sub.coef[i - j] = 1
            sub = sub * termo
            sub = sub * den
            # print('sub-> ',sub)
            sub.simplify()
            if sub.len() == 1 and sub[0] == 0 or sub.len() == 0:
                # print('final sub - >',sub)
                break
            div = div - sub
            # print('div-> ',div)

            ans.coef[i - j] += termo
            i = div.len() - 1
            j = den.len() - 1
        ans.simplify()
        return ans


a = Polinomio(1,0,1)
b = Polinomio(1,0)
c = a // b

print('f(x) =', a)
print('g(x) =', b)
print('h(x) = f(x)/g(x) =', c)
print('resto = ',a%b)
import re

# def getCoef(s):
#     pather = r'[-]{0,1}[0-9]*'
#     # If-statement after search() tests if it succeeded
#     print('found as', re.findall(pather, s))
#
#
#
# a = '-15x^2 15 20'
# getCoef(a)
