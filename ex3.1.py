import random

numeros = [random.randint(-500,501) for i in range(50)]
print(numeros)

def main(seq_numeros):
    pares = 0
    impares = 0
    for v in range(len(seq_numeros)):
        if (seq_numeros[v] % 2) == 0:
            pares = pares + 1
        else:
            impares = impares + 1
    return 'quantidade de pares: ' + str(pares) +  '. quantidade de ímpares: ' + str(impares)

print(main(numeros))


