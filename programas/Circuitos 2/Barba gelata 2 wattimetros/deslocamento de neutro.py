from libs import pc,s2c,plotFasor

def comNeutro(E,C):
    E = [s2c(i) for i in E]
    C = [s2c(i) for i in C]
    txt = ['a','b','c']
    I = [E[i]/C[i] for i in range(len(E))]
    In = sum(I)
    print('In = ',In)
    print(plotFasor(In,'IN','verdel'))

    for i in I:
        n = f'I{txt.pop(0)}'
        print(plotFasor(i,n,'vermelho'))
def semNeutro(E,C):
    E = [s2c(i) for i in E]
    C = [s2c(i) for i in C]
    txt = ['aN','bN','cN']
    VnN = sum([E[i]/C[i] for i in range(len(E))])/sum ([1/i for i in C])
    EfN = [i - VnN for i in E]
    print(plotFasor(VnN,'VnN','verdel'))

    for i in EfN:
        n = f'E{txt.pop(0)}'
        print(plotFasor(i,n,'amarelo'))




comNeutro(('57.7|0','57.7|-120','57.7|120'),(50,50+377j*160e-3,50+1/(377j*45.9e-6)))
# semNeutro(('57.7|0','57.7|-120','57.7|120'),(50,50+377j*160e-3,50+1/(377j*45.9e-6)))

