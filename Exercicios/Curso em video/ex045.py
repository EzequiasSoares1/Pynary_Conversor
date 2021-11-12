from random import randint

print('Escolha um numero:')
s = ('pedra', 'papel', 'tesoura')
print('-=-'*20)
print('''[0] Pedra
[1] Papel
[2] Tesoura''')
print('-=-'*20)
c = randint(0, 2)
d = int(input('Digite o numero:'))

if c != 0:#pedra
    if s == 0:
        print('Empatamos voçê colocou {}'.format(s[d]))
        print('E eu coloquei {}'.format(s[c]))
    elif s == 1:
        print('Voçê venceu')
        print('Voçê coloquei {}'.format(s[d]))
        print('E eu coloquei {}'.format(s[c]))
    elif s == 2:
        print('Eu venci')
        print('Voçê coloquei {}'.format(s[d]))
        print('E eu coloquei {}'.format(s[c]))

elif c != 1:#papel
    if s == 0:#pedra
        print('Eu venci')
        print('Voçê coloquei {}'.format(s[d]))
        print('E eu coloquei {}'.format(s[c]))
    elif s == 1:#papel
        print('Empatamos voçê colocou {}'.format(s[d]))
        print('E eu coloquei {}'.format(s[c]))

    elif s == 2:
        print('Voçê venceu')
        print('Voçê coloquei {}'.format(s[d]))
        print('E eu coloquei {}'.format(s[c]))

elif c != 2:#tesoura
    if s == 0:  # pedra
        print('Voçê venceu')
        print('Voçê coloquei {}'.format(s[d]))
        print('E eu coloquei {}'.format(s[c]))
    elif s == 1:  # papel
        print('eu venci')
        print('Empatamos voçê colocou {}'.format(s[d]))
        print('E eu coloquei {}'.format(s[c]))

    elif s == 2:
        print('Empatamos voçê colocou {}'.format(s[d]))
        print('E eu coloquei {}'.format(s[c]))