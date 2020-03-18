def openFile():
    import tkinter as tk
    from tkinter import filedialog
    root = tk.Tk()
    root.withdraw()
    filename = filedialog.askopenfilename()
    if filename == '':
        raise ValueError('i need a file')
    return filename


    
import re,os, ctypes,time


def dialogo(title, text, style=1):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

pat = r'[^\d| |\.|,|-]+'

lines = None;
filename = openFile()
begin = time.time()
with open(filename,'r') as file:
    title = file.readline()[:-1]
    lines = file.readlines()

def getName(text):
    a = ''
    try:
        a = re.findall('"(.*?)"',text)[0]
    except Exception as e:
        pass;
    
    return a
names = [getName(i) for i in lines]
lines = [re.sub('("(.*?)")|[=\n]','',i) for i in lines]
#print(lines)
#print(re.split('("(.*?)")','"ola"'))
#print(names)



# retira letras
def retiraErro(txt):
    if bool(re.search(r'\d',txt)):
        return re.sub(pat,'',txt).strip()
    else:
        return txt.strip()
lines = [retiraErro(i) for i in lines]

#separa  numeros
lines = [re.split(r'[\s]+',lt) for lt in lines]
print(lines)
#transforma o valor
for i in range(len(lines)):
    lines[i] = [j for j in lines[i]]
    
def tableTolatex(caption,names,elements,tab =''):
    print(elements)
    def cabecalho(names):
        s = ''
        for i in names:
            s+= f'|c'
        s+='|'
        return s
    def lineH():
        return tab+'          \hline %linha horizontal \n'
    def title(names):
        s = tab
        for i in range(len(names)):
            s+= f'{names[i]}'
            if i+1<len(names):
                s+=' & '
        s+=' \\\\\n'
        return s
    s = tab+ '\\begin{table}[H]\n'
    s += tab+'     \\centering\n'
    s  += tab+'    \\begin{tabular}{'+cabecalho(names)+'}\n'
    s += lineH()
    s += tab+'          '+title(names)
    s+= lineH()
    while  len(elements[0])>0:
        s+=tab+'      '
        for i in range(len(elements)):
            if i>0 :
                s+=' &'
            
            s+=f' {elements[i].pop(0) }'
        s+= tab+f' \\\\ \n{lineH()}'
    s+=tab+'    \end{tabular}\n'
    s+=tab+'    \\caption{'+f'{caption}'+'}\n'
    s+= tab+ '\\end{table}\n\n'
    return s

print(names)
for i in range(len(lines)):
    if i<len(names):
        if names[i]=='':
            print('missing name!')
            names.append(input(f'nome da variavel {i+1}: '))
if title == '':
    print('missing title name!')
    title = input('titulo da tabela: ')
tabela = tableTolatex(title,names,lines,'    ')

#with open(filename.replace('.txt','')+'_out.txt','w') as file:
#    file.write(tabela)
print('finalizado')

import pyperclip as clib

clib.copy(tabela)


dialogo("Tarefa finalizada",'o Texto foi copiado para a area de transferência.\n\ntempo gasto: %.5g ms'%(time.time()-begin),0)
#os.startfile('out.txt');
#print(tableTolatex('alguma media ai',['Medida[v]','corrente[y]'],lines,'      '))
