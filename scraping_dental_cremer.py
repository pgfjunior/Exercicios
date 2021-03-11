def scraping_precos (url):

    import requests
    from bs4 import BeautifulSoup

    page = requests.get(url).content
    soup = BeautifulSoup(page, 'html.parser')

    produtos = soup.find_all('span', class_='base')
    c=1
    nome_e_preco = []
    for produto in produtos:
        nome_e_preco.append(produto.get_text())

    precos = soup.find_all('span', class_="price")

    for preco in precos:
        if len(precos) == 1:
            nome_e_preco.append(preco.get_text())
        if len(precos) > 1 and c == 2:
            nome_e_preco.append(preco.get_text())
        c += 1
    
    print(nome_e_preco)