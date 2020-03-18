import cmath
from libs import *


class Circuito:
    def __init__(self, name, IL: (tuple, list), VL: (tuple, list) = None, Vn: (tuple, list) = None):
        if VL == Vn is None or (VL is not None and len(VL) != 3) or (Vn is not None and len(Vn) != 3):
            raise AttributeError('I need more info')
        self.ia = s2c(IL[0])
        self.ib = s2c(IL[1])
        self.ic = s2c(IL[2])
        self.name = name
        if VL is not None:
            self.eab = s2c(VL[0])
            self.ebc = s2c(VL[1])
            self.eca = s2c(VL[2])
        else:
            self.eaN = s2c(Vn[0])
            self.ebN = s2c(Vn[1])
            self.ecN = s2c(Vn[2])
            self.eab = self.eaN - self.ebN
            self.ebc = self.ebN - self.ecN
            self.eca = self.ecN - self.eaN
        self.seq = 'ABC'
        if cmath.phase(self.eab) - cmath.phase(self.ebc) < 0:
            self.seq = 'CBA'

    def __repr__(self):
        return f'   {self.seq}\n   ia, ib, ic = ({pc(self.ia)}) , ({pc(self.ib)}) , ({pc(self.ic)})\n' + \
               f'   Eab , Ebc, Ecb = ({pc(self.eab)}) , ({pc(self.ebc)}) , ({pc(self.eca)})'

    def __getitem__(self, item: slice):
        r = [item.start, item.stop, item.step]
        for i in range(len(r)):
            if r[i] is not None:
                r[i] = f'{r[i]}'.upper()
        if r[0] == 'I':
            if r[1] == 'A':
                return self.ia
            elif r[1] == 'B':
                return self.ib
            elif r[1] == 'C':
                return self.ic
            raise AttributeError('WTF! what you want? ')
        if r[0] == 'V' or r[0] == 'E':
            if r[1] == 'A':
                if r[2] == 'B':
                    return self.eab
                elif r[2] == 'C':
                    return -self.eca
                elif r[2] == 'N':
                    return self.eaN
                raise AttributeError('WTF! what you want? ')
            elif r[1] == 'B':
                if r[2] == 'A':
                    return -self.eab
                elif r[2] == 'C':
                    return self.ebc
                elif r[2] == 'N':
                    return self.ebN
                raise AttributeError('WTF! what you want? ')
            elif r[1] == 'C':
                if r[2] == 'B':
                    return -self.ebc
                elif r[2] == 'A':
                    return self.eca
                elif r[2] == 'N':
                    return self.ecN
                raise AttributeError('WTF! what you want? ')
        raise AttributeError('WTF! what you want? ')

    def w(self, i1: str, i2: str):
        i1 = i1.upper()
        i2 = i2.upper()
        if i1 == i2:
            raise AttributeError('WTF! what you want? ')
        i_s = [i1, i2]
        i, j, k = None, None, None
        if self.seq == 'ABC':
            if 'A' not in i_s:
                i, j, k = 'B', 'C', 'A'
            elif 'B' not in i_s:
                i, j, k = 'C', 'A', 'B'
            elif 'C' not in i_s:
                i, j, k = 'A', 'B', 'C'
        elif self.seq == 'CBA':
            if 'A' not in i_s:
                i, j, k = 'C', 'B', 'A'
            elif 'B' not in i_s:
                i, j, k = 'A', 'C', 'B'
            elif 'C' not in i_s:
                i, j, k = 'B', 'A', 'C'
        v = {}
        # 9898 ⚪
        # 9899 ⚫
        # 9900 ⚬
        v['desenho\n'] = [f'A ⚬{"_" * 5}', f'B ⚬{"_" * 5}', f'C ⚬{"_" * 5}', ]
        if 'A' in i_s:
            v['desenho\n'][0] += chr(0x26BA) * 3
        if 'B' in i_s:
            v['desenho\n'][1] += chr(0x26BA) * 3
        if 'C' in i_s:
            v['desenho\n'][2] += chr(0x26BA) * 3
        mx = max(len(v['desenho\n'][0]), len(v['desenho\n'][1]), len(v['desenho\n'][2]))
        for t in range(len(v['desenho\n'])):
            v['desenho\n'][t] += "_" * (mx - len(v['desenho\n'][t]) + 4) + '...'
        v['desenho\n'] = '\n' + v['desenho\n'][0] + '\n' + v['desenho\n'][1] + '\n' + v['desenho\n'][2] + '\n'

        v['W1  le corrente '] = f'{i1.upper()}'
        v['W2  le corrente '] = f'{i2.upper()}'
        v['i '] = i
        v['j '] = j
        v['k '] = k
        v[f'w[ik]:[{i + k}]'] = float((self['V':i:k] * self['i':i].conjugate()).real)
        v[f'w[jk]:[{j + k}]'] = float((self['V':j:k] * self['i':j].conjugate()).real)
        v[f'w[ij]:[{i + j}]'] = float((self['V':i:j] * self['i':i].conjugate()).real)
        v[f'w[ji]:[{j + i}]'] = float((self['V':j:i] * self['i':j].conjugate()).real)
        v['  '] = ''
        v['P[w]'] = v[f'w[ik]:[{i + k}]'] + v[f'w[jk]:[{j + k}]']
        v['Q[var]'] = (3 ** -0.5) * (
                2 * (v[f'w[ji]:[{j + i}]'] - v[f'w[ij]:[{i + j}]']) + v[f'w[ik]:[{i + k}]'] - v[f'w[jk]:[{j + k}]'])
        v[' '] = ''
        v[f'w[{i + k}]'] = f"Re({pc(self['V':i:k])} * {pc(self['i':i].conjugate())})"
        v[f'w[{j + k}]'] = f"Re({pc(self['V':j:k])} * {pc(self['i':j].conjugate())})"
        v[f'w[{i + j}]'] = f"Re({pc(self['V':i:j])} * {pc(self['i':i].conjugate())})"
        v[f'w[{j + i}]'] = f"Re({pc(self['V':j:i])} * {pc(self['i':j].conjugate())})"
        v['P[w] = '] = f"{pc(v[f'w[ik]:[{i + k}]'])} + {pc(v[f'w[jk]:[{j + k}]'])}"
        v[
            'Q[var] ='] = f"(3^-0.5) * (2 * ({pc(v[f'w[ji]:[{j + i}]'])} - {pc(v[f'w[ij]:[{i + j}]'])}) + {pc(v[f'w[ik]:[{i + k}]'])} - {pc(v[f'w[jk]:[{j + k}]'])})"
        return v

    def prt(self, i1, i2):
        s = ''
        mx = 0
        it = self.w(i1, i2).items()
        for k, v in it:
            mx = max(len(k), mx)
        for k, v in it:
            s += k + ' ' * (mx - len(k) + 1) + f'{pc(v)}\n'
        return s[:-1]


a = Circuito('barba gelata exercicio 1 da lista', ('43.5|116.6', '43.3|-48', '11.9|-114.2'),
             VL=('220|120', '220|0', '220|-120'))
# a = Circuito(('32.79|-5.55', '29.08|-178.13', '5.5|130.65'), VL=('208|0', '208|-120', '208|120'))

with open('out/' + a.name + '.txt', 'w', encoding='utf-8') as f:
    print(a, file=f)
    print('-' * 60, file=f)
    print(a.prt('a', 'b'), file=f)
    print('-' * 60, file=f)
    print(a.prt('b', 'c'), file=f)
    print('-' * 60, file=f)
    print(a.prt('c', 'a'), file=f)
