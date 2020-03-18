from Sites import *
import requests, os
path = '../out/Docentes/'
profs = Docente.load_list(f'{path}profs.bin')  # le a lista de Docentes
# Baixar pdfs
for prof in profs:
    print('Baixando pdf de ', prof.name)
    for v, i in prof.link_pdf_plano_de_ensino.items():
        print('\t',f'{v}.pdf',end='  ')
        pdf = requests.get(i)
        if not os.path.exists(path + prof.name):
            os.makedirs(path + prof.name)
        with open(path + prof.name + f'/{v}.pdf', 'wb') as pdf_file:
            pdf_file.write(pdf.content)
        print('sucesso!')



