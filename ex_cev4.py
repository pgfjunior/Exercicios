"""PEDRA, PAPEL E TESOURA"""

from random import randint
from time import sleep

lista = ['PEDRA', 'PAPEL', 'TESOURA']
jogada_computador = lista[randint(0,2)]
jogada_participante = 0

while jogada_participante > 3 or jogada_participante < 1:
    jogada_participante = int(input(''' DIGITE O NUMERO CORRESPONDENTE A SUA JOGADA: 
1 - PEDRA
2 - PAPEL
3 - TESOURA
'''))

    if jogada_participante == 1:
        jogada_participante = 'PEDRA'
        break
    elif jogada_participante == 2:
        jogada_participante = 'PAPEL'
        break
    elif jogada_participante == 3:
        jogada_participante = 'TESOURA'
        break
    else: 
        print('Jogada inválida, tente novamente')

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(2)

if jogada_computador == jogada_participante:
    print('Você jogou {} e eu joguei {}. EMPATAMOS ESSA!'.format(jogada_participante, jogada_computador))
elif (jogada_computador == 'PEDRA' and jogada_participante == 'TESOURA') or (jogada_computador == 'PAPEL' and jogada_participante == 'PEDRA') or (jogada_computador =='TESOURA' and jogada_participante == 'PAPEL'):
    print('Você jogou {} e eu joguei {}. Você perdeu!'.format(jogada_participante, jogada_computador))
else: 
    print('Você jogou {} e eu joguei {}. PARABÉNS, você ganhou essa!!'.format(jogada_participante, jogada_computador))