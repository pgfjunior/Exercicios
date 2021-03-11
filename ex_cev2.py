from datetime import date
nascimento = int(input('Digite o ano de nascimento do atleta: '))
atual = date.today().year 
idade = atual - nascimento
print('O atleta tem {} anos de idade'.format(idade))

if idade <= 9:
    print('O Atleta pertence a categoria MIRIM')
elif idade <= 14:
    print('O Atleta pertence a categoria INFANTIL')
elif idade <= 19:
    print('O Atleta pertence a categoria JUNIOR')
elif idade <= 25:
    print('O Atleta pertence a categoria SENIOR')
else: 
    print('O Atleta pertence a categoria MASTER')