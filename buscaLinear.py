import random

numeros = []

for i in range(0,50):
    v = random.randint(0,100)
    numeros.append(v)

numero = int(input('Digite um numero a ser encontrado: '))

if numero in numeros:
    print('o numero digitado se encontra na lista "números" no índice: ' + str(numeros.index(numero)))
else: 
    print("-1")    
print(5%2)