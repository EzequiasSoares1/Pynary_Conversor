from datetime import date
a = int(input('Quantos anos você nasceu:'))
s = date.today().year
r = s - a

if r < 18:
    f = 18 - r
    print('Ainda nao chegou o tempo de se alistar restam {} anos'.format(f))

elif r == 18:
    print(' chegou o tempo de seu alistar vaga a uma brigada militar')

elif r > 18:
    g = r - 18
    k = s - g
    print('Seu alistamento foi em {} já fazem {} anos'.format(k, g))
