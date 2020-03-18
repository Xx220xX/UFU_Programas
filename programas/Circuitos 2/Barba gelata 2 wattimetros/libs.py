from math import *
import cmath
import scipy as sp
import numpy as np


def s2c(c: str):

    if isinstance(c, (float, int, complex)):
        return c
    if not isinstance(c, str):
        raise ValueError(f'not suport to {type(c)}')
    if not '|' in c:
        return complex(c.replace(' ', '').replace('i', 'j'))
    c = c.split('|', 1)
    if len(c) == 0:
        c = [0, 0]
    elif len(c) == 1:
        c.append(0)
    c = [float(i) for i in c]
    c[1] = c[1] * pi / 180
    return complex(round(c[0] * cos(c[1]), 10), round(c[0] * sin(c[1]), 10))


def pc(c: complex, precisao=4):
    if isinstance(c, (int, float)):
        return f'%.{precisao}f' % c
    elif isinstance(c, str):
        return c
    return f'%.{precisao}g|%.{precisao}f°' % (abs(c), cmath.phase(c) * 180 / pi)

def plotFasor(c,name,color = (255,255,255)):
    if isinstance(color,str):
        color = {'verde':(0,255,0),
                 'verde1':(50,205,50),
                 'verde2':(34,139,34),
                 'verde3':(0,128,0),
                 'verde4':(0,100,0),
                 'verdel':(0,250,154),
                 'verdel1':(0,255,127),

                 'azul':(0,0,255),
                 'azul1':(0,0,205),
                 'azul2':(0,0,139),
                 'azul3':(105,89,205),
                 'azul4':(131,111,255),
                 'azull':(0,255,255),
                 'azull1':(0,206,209),  
                 
                 'vermelho':(255,0,0),
                 'vermelho1':(178,34,34),
                 'vermelho2':(220,20,60),
                 'vermelho3':(233,150,122),
                 
                 'amarelo':(255,255,0),
                 'amarelo1':(255,215,0),
                 'laranja':(255,140,0),
                 'laranja1':(255,165,0),
                 }[color]
    return f'fasor.add("{name}",{abs(c)},{cmath.phase(c)*180/pi},color{color})'
class Matrix(object):
    def __init__(self, data: (list, int) = None, size_i: int = None, size_j: int = None):
        if data is None and size_i is None and size_j is None:
            raise AttributeError('Falta coisa ai man')

        if isinstance(data, Matrix):
            self.data = data.data.copy()
        if isinstance(data, np.ndarray):
            data = data.tolist()

        if isinstance(data, (int, float)):
            size_j = size_i
            size_i = data
            data = None

        if isinstance(data, list):
            try:
                len(data[0])
            except TypeError:
                data = [data]
        if size_i is None:
            size_i = len(data)
        if size_j == None:
            try:
                size_j = len(data[0])
            except TypeError:
                size_j = 1
        if data is None:
            self.data = np.array([[0] * size_j] * size_i)
        if data:
            m = []

            leni = len(data)
            lenj = len(data)
            for i in range(size_i):
                m.append([])
                for j in range(size_j):
                    if i < leni and j < lenj:
                        m[i].append(s2c(data[i][j]))
                    else:
                        m[i].append(0)
            self.data = np.array(m)

    def __repr__(self):
        lt = []
        m = 0
        for i in self.data.tolist():
            lt.append([])
            for j in i:
                lt[-1].append(pc(j,precisao=4))
                m = max(len(lt[-1][-1]), m)
        s = ''
        for i in lt:
            for j in i:
                t = (m - len(j)) // 2
                s += ' ' * t + j + '    ' + ' ' * t
            s+='\n'
        return s

    def __mul__(self, other):
        # print(isinstance(self.data,np.ndarray))
        a = self.data * other.data
        return Matrix(a)

    def transpose(self):
        return Matrix(self.data.transpose())

    def inverse(self):
        return Matrix(np.linalg.inv(self.data))
