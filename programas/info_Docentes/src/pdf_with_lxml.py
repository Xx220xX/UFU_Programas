from Sites import *

'''
pip install tabula-py
pip install -U selenium
'''
profs = Docente.load_list('Docentes/profs.bin')  # le a lista de Docentes

import pdfx, re


def extractPage(string):
    return re.split(r'Página \d de \d', string)


def removeHoras(string):
    return re.sub(r'(\d+ h \d+ min)', '', string)


def removeExcessLines(string):
    return re.sub(r'(\n){2,}', '\n', string)


for prof in profs:
    try:
        pdf = pdfx.PDFx('Docentes/' + prof.name + '/2018 - 2.pdf')
    except Exception as e:
        print(e)
        print(f'{prof.name} não possui informaçao')
        break
        continue

    # print(pdf.get_text())
    pages = extractPage(pdf.get_text())
    pages[0] = removeHoras(pages[0])
    pages[0] = removeExcessLines(pages[0])
    print(pages[0])
    print('================================')

