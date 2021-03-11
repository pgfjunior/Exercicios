def main():
    
    n = int(input('digite um numero inteiro para saber se ele é triangular: '))
    x = 0
    prod = 0
    while x < (n/3):
        prod = x*(x+1)*(x+2)
        if prod == n:
            return 'o numero ' + str(n) + ' é triangular'
            break
        else: 
            x = x+1
    return 'o numero ' + str(n) + ' não é triangular'

print(main())