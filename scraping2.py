import requests
from bs4 import BeautifulSoup

lista_de_urls_dos_produtos=['https://www.dentalcremer.com.br/compressa-de-gaze-ultracotton-9-fios-n-o-esteril-ultracotton-100545.html', 'https://www.dentalcremer.com.br/sugador-descartavel-transparente-allprime-127720.html', 'https://www.dentalcremer.com.br/tira-de-lixa-de-poliester-microdont-513202.html','https://www.dentalcremer.com.br/anestesico-lidostesim-3-1-50-000-dla.html']
lista_de_urls_dos_produtos.sort()

for url in lista_de_urls_dos_produtos:
    page = requests.get(url).content
    soup = BeautifulSoup(page, 'html.parser')

    produtos = soup.find_all('span', class_='base')
    for produto in produtos:
        print(produto.get_text())

    precos = soup.find_all('span', class_="price")
    for preco in precos:
        print(preco.get_text())