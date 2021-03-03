import random
import statistics

numeros = []

for i in range(0,100):
    v = random.randint(1,1000)
    numeros.append(v)

numeros.sort()
mediana_numeros = statistics.median(numeros)

