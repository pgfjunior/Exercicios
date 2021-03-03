def main():
    n = int(input('digite um inteiro maior que zero: '))
    fatorial = n
    while n > 1:
        n = n - 1
        fatorial = fatorial * n
    print(fatorial)

main()       
