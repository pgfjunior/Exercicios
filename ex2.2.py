def main():
    num = int(input('digite um valor inteiro: '))
    soma = 0
    
    while num != 0:
        soma = soma + num
        num = int(input('digite um valor inteiro: '))

    print('A soma é', soma)

main()
