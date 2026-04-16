from random import randint
from time import sleep
computador = randint(0,5) # Faz o computador 'PENSAR'
print('-=-' *10)
print('Vou pensar em um número de 0 a 5 . Tente advinhar')
print('-=-'* 10)
jogador = int(input('Em que eu número eu pensei?')) # Jogador tenta avinhar
print('PROCESSANDO..')
sleep(3)
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer')
else:
    print('Ganhei! Eu pensei no número {} e você no número {}'.format(computador, jogador))
