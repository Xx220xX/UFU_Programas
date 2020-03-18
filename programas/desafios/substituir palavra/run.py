import  re
def replaceLast1(inp, old, replace):
    size = len(inp)
    for i in range(size):
        if old in inp[size - i:]:
            return inp[:size - i] + inp[size - i:].replace(old, replace)


print(replaceLast1('Quem parte e reparte fica com  a maior parte', 'parte', 'parcela'))


# out>> Quem parte e reparte fica com  a maior parcela
# nao é tao bom

def replaceLast2(inp, old, replace):
    words = inp.split(' ')[::-1]
    for i in range(len(words)):
        if old == words[i]:
            words[i] = replace
            return ' '.join(words[::-1])


print(replaceLast2('Quem parte e reparte fica com  a maior parte', 'parte', 'parcela'))
# out>> Quem parte e reparte fica com  a maior parcela

# usando expressao regular da para fazer em uma linha
# def replaceLast2(inp, old, replace):
#     inp = inp[::-1]
#     out = re.sub(old[::-1],)
# print(replaceLast3('Quem parte e reparte fica com  a maior parte', 'parte', 'parcela'))
# # out>> Quem parte e reparte fica com  a maior parcela