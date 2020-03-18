# objetivos abrir arquivos dos docentos
# captura qualquer arquivo que tenha notas
import os
from Sites import *
# pegar site da feelt


print('abrindo site felt')
site_Feelt = requests.get('http://www.feelt.ufu.br/pessoas/docentes')
if site_Feelt.status_code == 200:
    print('Sucesso ao abrir site')
else:
    raise FileExistsError('não foi possivel acessar o site')

print('extraindo dados')
profs = extrair_docentes(site_Feelt)
# printar aquivos

with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(re.sub(r'[\[\]]|(,\x20)', '\n', str(profs)))
print('Salvando dados')
if not os.path.exists('../out/Docentes/'):
    os.makedirs('../out/Docentes/')
Docente.salve_list(profs,'../out/Docentes/profs.bin')
print('Programa finalizado')
