def main():
    n = input('digite um valor de n (n>0): ')
    d = input('digite um valor de d (0<=d<=9): ')
    quantidade = 0
    
    for i in range(len(n)):
        if n[i] == d:
            quantidade = quantidade + 1

    return 'o dígito ' + str(d) + ' ocorre ' + str(quantidade) + ' vezes em ' + str(n)

print(main())