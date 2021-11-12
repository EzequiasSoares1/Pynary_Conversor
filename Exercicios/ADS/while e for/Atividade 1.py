from time import sleep
for c in range(5):
    d = int(input('Digite um numero:'))
    if d > 0 and d <= 42 :
        print('O numero é positivo')
    elif d >= 44:
        print('O numero é positivo')
    elif d == 0:
        print('O numero é igual a zero')
    elif d < 0:
        print('O numero é negativo')
    elif d == 43:
        sleep(4)
