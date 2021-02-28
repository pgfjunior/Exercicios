numeros = [i for i in range(100,0,-1)]

numero = int(input('Digite um numero de 0 a 100 a ser encontrado: '))

if numero in numeros:
    print('o numero digitado se encontra na lista "números" no índice: ' + str(numeros.index(numero)))
else: 
    print("-1")    