import random

numeros=[random.randint(1,1000) for i in range(0,50)]

print(numeros)

valor_buscado = int(input('digite um valor a ser buscado: '))

def busca_sequencial(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return 'o valor está no índice: ' + str(i) 
    return -1

print(busca_sequencial(numeros, valor_buscado))
