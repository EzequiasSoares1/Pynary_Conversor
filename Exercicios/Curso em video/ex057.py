from random import choice
from time import sleep
print('-'*40)
print('vou pensar em um numero entre 0 e 10')
print('-'*40)

cont = 1

c = int(input('em que numero estou pensando:'))
print('processando...')
sleep(0.5)


s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r = choice(s)
print(r)

while c != r:
    
    if c > r:
        c = int(input('é menor, digite novamente:'))

    elif c < r:
        c = int(input('é maior, digite novamente:'))

    cont += 1

print('Acertou no {} palpite. Parabens!!!'.format(cont))



