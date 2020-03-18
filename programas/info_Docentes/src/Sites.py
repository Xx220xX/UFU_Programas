import requests
from bs4 import BeautifulSoup  # pip install bs4
import re
import pickle
import time

index = 0


def capturarDado(padrao, input_str, inicio, fim):
    dado = re.search(padrao, input_str)
    try:
        dado = dado.group(0)[inicio:fim].strip()
    except AttributeError:
        return None
    return dado


class Docente:
    def __init__(self, name, status, lates, email, telefone, link_do_docente=None, faculdade=None,
                 plano_de_ensino=None):
        # self.inf = {'Name': name, 'Status': status, 'Curriculo lates': lates, 'email': email, 'Telefone': telefone}
        global index
        self.name = name
        self.status = status
        self.lates = lates
        self.email = email
        self.telefone = telefone
        self.faculdade = faculdade
        self.link_do_docente = link_do_docente
        self.plano_de_ensino = plano_de_ensino
        index = index + 1
        self.link_pdf_plano_de_ensino = {}
        self.index = index

    def __repr__(self):
        s = ''
        for k, v in self.__dict__.items():
            # if v is None  and k != 'plano_de_ensino':
            #     print('para : ', self.name, k, 'foi vazio')
            if v is not None:
                s += f'{k} : {v}\n'
        return s + '\n'

    def tableMarkdown(self):
        return f'| {self.name} | {self.telefone} | {self.email} | {self.status}  | {self.faculdade} | [link]({self.lates}) |'

    def getPlanoDocente(self):
        # Verificacao de segurnca
        if self.link_do_docente is None:
            return self
        # abrindo site
        site_do_docente = requests.get(self.link_do_docente)
        # verificacao de seguranca
        if site_do_docente.status_code != 200:
            print('falha')
            self.link_pdf_plano_de_ensino = 'falha'
            return self

        soup = BeautifulSoup(site_do_docente.content, 'html.parser')
        # estraindo bloco contendo os links
        block_contendo_pdf = str(soup.find(name='div', attrs={'class': 'view-content'}))
        soup = BeautifulSoup(block_contendo_pdf, 'html.parser')
        block_contendo_pdf = soup.findAll(name='a')
        for plano in block_contendo_pdf:
            ano = capturarDado(r'>[ºa-zA-Z0-9\x20-]+<', str(plano), 1, -1)  # captura data no formato dddd - d° semestre
            ano = ano.replace('º semestre', '').strip()
            link_pdf = capturarDado(r'"http[\w/:\+-\?_\.]+"', str(plano), 1, -1)  # captura o link do pdf
            self.link_pdf_plano_de_ensino.update({ano: link_pdf})
        return self

    def salve(self, output_name):
        with open(output_name, 'wb') as output:  # Overwrites any existing file.
            pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def salve_list(lista, output_file_name):
        with open(output_file_name, 'wb') as f:
            pickle.dump(lista, f)

    @staticmethod
    def load_list(input_file):
        with open(input_file, 'rb') as input:
            load = pickle.load(input)
        return load


def extrair_docentes(html):
    ti = time.time()
    profs = []
    # pegar div dos docentes
    soup = BeautifulSoup(html.content, 'html.parser')
    div_dos_profs = soup.findAll('div', {
        "class": ["views-row-even separar-thumb", 'views-row-odd views-row-first separar-thumb',
                  'views-row-odd separar-thumb']})
    # iterar em todos os dados
    print("isso pode demorar\nPor favor espere!")
    for data in div_dos_profs:
        html = f"""<html>
            <head>
            <title>Employee Profile</title>
            <meta charset="utf-8"/>
            </head> 
            <body>
            {data}
            </body>
            </html>
            """
        soup = BeautifulSoup(html, features="html.parser")
        # pegar as div que contem os dados
        name = soup.find(name='h3', attrs={"class": "titulo"})
        status = soup.find(name='span', attrs={"class": "cargo"})
        lates = soup.find(name='a', attrs={"target": "_blank"})
        telefone = soup.find(name='div',
                             attrs={'class': 'field field-name-info-contato field-type-ds field-label-hidden'})
        email = soup.find(name='a', attrs={"target": None, 'href': re.compile(r'mailto:.+')})
        faculdade = soup.find(name='div', attrs={
            "class": "field field-name-field-curso field-type-taxonomy-term-reference field-label-hidden"})

        # usar expressao regular para estrair as informacoes
        link_arquivos_docente = 'http://www.feelt.ufu.br' + capturarDado(r'"/[\w:0-9/\.\?=-]+"', str(name), 1, -1)
        name = capturarDado(r'>[\w\s]+<', str(name), 1, -1)
        status = capturarDado(r'>[\w\s]+<', str(status), 1, -1)
        lates = capturarDado(r'"[\w:0-9/\.\?=]+"', str(lates), 1, -1)
        telefone = capturarDado(r'>[\+\-\d\s]+<', str(telefone), 1, -1)
        email = capturarDado(r':[@\w\.]+', str(email), 1, None)
        faculdade = capturarDado(r'>([\w\sÁ-ú]{2,})<', str(faculdade), 1, -1)
        profs.append(
            Docente(name, status, lates, email, telefone, link_arquivos_docente, faculdade, ).getPlanoDocente())
        print('.', end='')
    print('\nDados extraídos')
    print(f'Tempo gasto {time.time() - ti} s')
    return profs
