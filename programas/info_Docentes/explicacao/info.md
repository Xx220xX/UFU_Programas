
## Extrair 
[Arquivo completo](src/Sites.py)
> chamada da funcao
> ```python
> profs = extrair_docentes(site_Feelt)
> ```


## definição da função
> recebe um html gerado por request.get
```python
def extrair_docentes(html):
```
> Lista para armazenar dados dos docentes

```python
    profs = []
```

####  pegar div dos docentes

```python
    soup = BeautifulSoup(html.content, 'html.parser')
    div_dos_profs = soup.findAll('div', {
        "class": ["views-row-even separar-thumb", 'views-row-odd views-row-first separar-thumb',
                  'views-row-odd separar-thumb']})
```
#### iterar em todos os dados
> Encontra informacoes atravez de padrões
```python    
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
    return profs
```
