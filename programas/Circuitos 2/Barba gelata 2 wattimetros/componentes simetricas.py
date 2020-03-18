import numpy as np

from libs import *

a = s2c('1|120')
T = Matrix([[1] * 3, [1, a ** 2, a], [1, a, a ** 2]])  # matrix de transformacao


def real2Sime(input: (Matrix, list)):
    input = Matrix(input).transpose()
    global T
    return T.inverse() * input


r = real2Sime(['100', '100|-120', '100|120'])
print(r)
