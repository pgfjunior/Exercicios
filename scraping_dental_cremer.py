def scraping_precos (url):

    import requests
    from bs4 import BeautifulSoup

    page = requests.get(url).content
    soup = BeautifulSoup(page, 'html.parser')

    produtos = soup.find_all('span', class_='base')
    c=1
    for produto in produtos:
        print(produto.get_text())

    precos = soup.find_all('span', class_="price")

    for preco in precos:
        if len(precos) == 1:
            print(preco.get_text())
        if len(precos) > 1 and c == 2:
            print(preco.get_text())
        c += 1