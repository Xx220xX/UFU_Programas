## Modulo a ser usado
```python
import pandas  # pip install pandas
import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install bs4
```
## Abrindo site da feelt
```python
site_Feelt = requests.get('http://www.feelt.ufu.br/pessoas/docentes')
if site_Feelt.status_code == 200:
    print('Sucesso ao abrir site')
else:
    raise FileExistsError('não foi possivel acessar o site')
```
