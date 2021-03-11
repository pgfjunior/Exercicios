nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2)/2
print('Suas notas foram {:.1f} e {:.1f} e sua média foi {:.1f}'.format(nota1, nota2, media))

if media < 5:
    print('Reprovado')
elif media >= 5 and media < 7:
    print('Recuperação')
else:
    print('Aprovado')